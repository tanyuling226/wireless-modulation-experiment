# QPSK调制原理

## 什么是QPSK？

QPSK（Quadrature Phase Shift Keying，正交相移键控）是BPSK的扩展，使用四个相位状态来传输数字信息，频谱效率是BPSK的两倍。

## 调制原理

### 基本映射

QPSK将**每2个比特**映射到**一个符号**，使用四个相位状态：

**格雷码映射**（推荐，相邻符号只有1位差异）：

| 比特对 | 相位 | 符号（归一化） |
|--------|------|----------------|
| 00     | 45°  | $(1+j)/\sqrt{2}$ |
| 01     | 135° | $(-1+j)/\sqrt{2}$ |
| 11     | 225° | $(-1-j)/\sqrt{2}$ |
| 10     | 315° | $(1-j)/\sqrt{2}$ |

数学表达式：

$$
s(t) = A \cos\left(2\pi f_c t + \phi_i\right)
$$

其中 $\phi_i \in \{45°, 135°, 225°, 315°\}$

### 星座图

QPSK的星座图有四个点，均匀分布在单位圆上：

```
    虚部(Q)
       |
   01  |  00
       |
-------+------- 实部(I)
       |
   11  |  10
       |
```

四个符号相位相差90°。

## 复数表示

使用复数表示QPSK符号更加简洁：

$$
s = I + jQ
$$

其中：
- $I$ 是同相分量（In-phase）
- $Q$ 是正交分量（Quadrature）

归一化后，每个符号的能量为1：$|s|^2 = 1$

## 为什么使用格雷码？

格雷码（Gray Code）的特点是**相邻符号只有1位不同**。

**好处**：当噪声导致符号判决错误时，通常是判决到相邻的符号点，使用格雷码可以确保只有1个比特错误，而不是2个。

**示例**：
- 自然码：00 → 01 → 10 → 11（相邻差2位）
- 格雷码：00 → 01 → 11 → 10（相邻差1位）

## 优点

1. **频谱效率高**：每个符号传输2比特信息
2. **性能较好**：在相同误符号率下，误比特率比自然码低
3. **应用广泛**：WiFi、LTE等系统的基础调制方式

## 缺点

1. **实现稍复杂**：需要I/Q两路处理
2. **抗噪声性能低于BPSK**：符号点距离较近

## Python实现要点

实现QPSK调制的关键步骤：

### 方法1：查表法

```python
# 定义格雷码映射字典
gray_map = {
    (0, 0): (1 + 1j) / np.sqrt(2),
    (0, 1): (-1 + 1j) / np.sqrt(2),
    (1, 1): (-1 - 1j) / np.sqrt(2),
    (1, 0): (1 - 1j) / np.sqrt(2)
}

# 每2比特查表
symbols = []
for i in range(0, len(bits), 2):
    bit_pair = (bits[i], bits[i+1])
    symbols.append(gray_map[bit_pair])
```

### 方法2：数学计算

```python
# 将比特序列reshape成(N/2, 2)
bit_pairs = bits.reshape(-1, 2)

# 分别计算I和Q分量
I = np.where(bit_pairs[:, 0] == 0, 1, -1)
Q = np.where(bit_pairs[:, 1] == 0, 1, -1)

# 格雷码映射（交换Q的符号）
Q = np.where(bit_pairs[:, 0] == 1, -Q, Q)

# 组合并归一化
symbols = (I + 1j * Q) / np.sqrt(2)
```

## 解调原理

QPSK解调使用**最小欧氏距离判决**：

1. 计算接收符号到所有参考点的距离
2. 选择距离最小的参考点
3. 输出该参考点对应的比特对

$$
\hat{s} = \arg\min_{s_i} |r - s_i|^2
$$

## 理论性能

在AWGN信道下，QPSK的误符号率（SER）为：

$$
P_s \approx 2Q\left(\sqrt{\frac{E_s}{N_0}}\right)
$$

由于使用格雷码，误比特率约为：

$$
P_b \approx \frac{1}{2}P_s
$$

## I/Q调制解释

QPSK可以看作两路独立的BPSK：

$$
s(t) = I \cos(2\pi f_c t) - Q \sin(2\pi f_c t)
$$

- **I路**：同相载波，$\cos(2\pi f_c t)$
- **Q路**：正交载波，$\sin(2\pi f_c t)$（相位差90°）

## 应用场景

QPSK广泛应用于：
- 卫星通信
- WiFi（IEEE 802.11）
- LTE/5G移动通信
- 数字电视广播（DVB）

## 参考资料

1. Proakis, J. G. (2008). *Digital Communications* (5th ed.). McGraw-Hill.
2. [Wikipedia - QPSK](https://en.wikipedia.org/wiki/Phase-shift_keying#Quadrature_phase-shift_keying_(QPSK))
