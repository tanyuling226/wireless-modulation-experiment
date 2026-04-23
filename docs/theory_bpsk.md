# BPSK调制原理

## 什么是BPSK？

BPSK（Binary Phase Shift Keying，二进制相移键控）是最简单的数字调制方式之一。它通过改变载波的相位来传输数字信息。

## 调制原理

### 基本映射

BPSK使用两个相位状态来表示二进制数据：

- **比特 0** → 相位 **0°** → 符号 **+1**
- **比特 1** → 相位 **180°** → 符号 **-1**

数学表达式：

$$
s(t) = 
\begin{cases}
A \cos(2\pi f_c t), & \text{比特为 0} \\
-A \cos(2\pi f_c t), & \text{比特为 1}
\end{cases}
$$

其中：
- $A$ 是信号幅度
- $f_c$ 是载波频率
- $t$ 是时间

### 星座图

BPSK的星座图非常简单，只有两个点：

```
    虚部(Q)
       |
       |
   -1  |  +1   实部(I)
-------+-------
       |
       |
```

两个符号在实轴上，相位相差180°。

## 优点

1. **实现简单**：只需要判断相位是0°还是180°
2. **抗噪声性能好**：两个符号点距离最远，不容易混淆
3. **解调容易**：只需要判断实部的正负

## 缺点

1. **频谱效率低**：每个符号只传输1比特信息
2. **数据速率低**：在相同带宽下，传输速率是QPSK的一半

## 应用场景

BPSK常用于：
- 深空通信（信噪比极低的环境）
- RFID标签
- 卫星通信
- 低速数据传输

## Python实现要点

实现BPSK调制的关键步骤：

1. **映射比特到符号**
   ```python
   symbols = np.where(bits == 0, 1, -1)
   ```

2. **或者使用数学运算**
   ```python
   symbols = 1 - 2 * bits
   ```

3. **转换为复数（保持接口一致性）**
   ```python
   symbols = symbols.astype(complex)
   ```

## 解调原理

BPSK解调非常简单：

$$
\hat{b} = 
\begin{cases}
0, & \text{if } \text{Re}(r) > 0 \\
1, & \text{if } \text{Re}(r) \leq 0
\end{cases}
$$

其中 $r$ 是接收到的符号（可能含噪声）。

## 理论性能

在AWGN（加性高斯白噪声）信道下，BPSK的误比特率（BER）为：

$$
P_e = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)
$$

其中：
- $E_b$ 是每比特能量
- $N_0$ 是噪声功率谱密度
- $Q(x)$ 是Q函数

## 参考资料

1. Proakis, J. G., & Salehi, M. (2008). *Digital Communications* (5th ed.). McGraw-Hill.
2. [维基百科 - 相移键控](https://zh.wikipedia.org/wiki/%E7%9B%B8%E7%A7%BB%E9%94%AE%E6%8E%A7)
