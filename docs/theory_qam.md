# 16-QAM调制原理

## 什么是QAM？

QAM（Quadrature Amplitude Modulation，正交幅度调制）同时改变载波的**幅度**和**相位**来传输信息。16-QAM使用16个不同的符号，每个符号传输4比特。

## 调制原理

### 基本映射

16-QAM将**每4个比特**映射到**一个符号**，使用16个不同的幅度-相位组合：

| I/Q分量 | 比特 | 符号值（归一化前） |
|---------|------|-------------------|
| I: 00   | 00xx | +3 |
| I: 01   | 01xx | +1 |
| I: 11   | 11xx | -1 |
| I: 10   | 10xx | -3 |

同样的规则适用于Q分量（后2位）。

### 星座图

16-QAM的星座图是一个4×4的方阵：

```
    虚部(Q)
       |
   +3  • • • •
   +1  • • • •  实部(I)
   -1  • • • •
   -3  • • • •
       |
```

16个符号均匀分布在方格点上。

### 归一化

为了使平均功率为1，需要进行归一化：

**未归一化的平均功率**：
$$
P_{avg} = \frac{1}{16} \sum_{i,q} (I^2 + Q^2) = \frac{2 \times (3^2 + 1^2 + 1^2 + 3^2)}{16} = \frac{2 \times 20}{16} = 2.5
$$

等等，让我重新计算...

每个I/Q分量的平均功率：
$$
P_I = \frac{3^2 + 1^2 + 1^2 + 3^2}{4} = \frac{20}{4} = 5
$$

总平均功率：$P_{total} = 2 \times 5 = 10$

**归一化因子**：$\sqrt{10}$

**归一化后的符号**：
$$
s = \frac{I + jQ}{\sqrt{10}}
$$

## 格雷码映射

16-QAM也使用格雷码映射，确保相邻符号只有1位差异：

| 比特（I路） | I分量 |
|-------------|-------|
| 00          | +3    |
| 01          | +1    |
| 11          | -1    |
| 10          | -3    |

同样的映射用于Q路（后2位）。

## 优点

1. **频谱效率高**：每个符号传输4比特，是QPSK的两倍
2. **数据速率高**：在相同带宽下传输更多数据
3. **广泛应用**：现代通信系统的标配

## 缺点

1. **抗噪声性能差**：符号点之间距离较近
2. **需要更高的SNR**：相比BPSK和QPSK
3. **实现复杂**：需要更精确的幅度控制

## Python实现要点

### 方法1：分离I/Q路处理

```python
# 将比特序列reshape成(N/4, 4)
bit_groups = bits.reshape(-1, 4)

# 前2位映射到I分量
i_bits = bit_groups[:, :2]
# 后2位映射到Q分量
q_bits = bit_groups[:, 2:]

# 格雷码映射函数
def gray_to_level(b0, b1):
    """格雷码映射：00→+3, 01→+1, 11→-1, 10→-3"""
    if b0 == 0 and b1 == 0:
        return 3
    elif b0 == 0 and b1 == 1:
        return 1
    elif b0 == 1 and b1 == 1:
        return -1
    else:  # b0 == 1 and b1 == 0
        return -3

# 对每组比特应用映射
I = np.array([gray_to_level(i[0], i[1]) for i in i_bits])
Q = np.array([gray_to_level(q[0], q[1]) for q in q_bits])

# 组合并归一化
symbols = (I + 1j * Q) / np.sqrt(10)
```

### 方法2：使用字典映射

```python
# 定义完整的格雷码映射
gray_map = {
    (0, 0): 3,
    (0, 1): 1,
    (1, 1): -1,
    (1, 0): -3
}

# 映射I和Q分量
bit_groups = bits.reshape(-1, 4)
I = np.array([gray_map[(b[0], b[1])] for b in bit_groups])
Q = np.array([gray_map[(b[2], b[3])] for b in bit_groups])

symbols = (I + 1j * Q) / np.sqrt(10)
```

## 解调原理

16-QAM解调也使用最小欧氏距离判决，但可以简化：

**方法1：穷举搜索**
- 计算到所有16个参考点的距离
- 选择最小距离对应的符号

**方法2：分离判决**（更快）
- 分别对I路和Q路进行判决
- I路：判断实部属于{-3, -1, +1, +3}中的哪一个
- Q路：判断虚部属于{-3, -1, +1, +3}中的哪一个

```python
def demodulate_component(value):
    """判决单个分量"""
    value_scaled = value * np.sqrt(10)  # 反归一化
    
    if value_scaled > 2:
        return (0, 0)  # +3 → 00
    elif value_scaled > 0:
        return (0, 1)  # +1 → 01
    elif value_scaled > -2:
        return (1, 1)  # -1 → 11
    else:
        return (1, 0)  # -3 → 10
```

## 性能特性

### 符号功率分布

16-QAM的符号功率不均匀：

- **角点**（4个）：功率最大 = $(3^2 + 3^2) / 10 = 1.8$
- **边点**（8个）：功率中等 = $(3^2 + 1^2) / 10 = 1.0$
- **内点**（4个）：功率最小 = $(1^2 + 1^2) / 10 = 0.2$

平均功率 = 1.0（已归一化）

### 误比特率

在AWGN信道下，16-QAM的近似误比特率：

$$
P_b \approx \frac{3}{8}Q\left(\sqrt{\frac{4E_s}{10N_0}}\right)
$$

## 更高阶的QAM

- **64-QAM**：8×8方阵，每符号6比特
- **256-QAM**：16×16方阵，每符号8比特
- **1024-QAM**：32×32方阵，每符号10比特

阶数越高，频谱效率越高，但对SNR要求也越高。

## 应用场景

16-QAM及更高阶QAM应用于：
- **WiFi**：802.11n/ac/ax
- **LTE/5G**：根据信道质量自适应选择调制方式
- **数字电视**：DVB-C/DVB-T
- **有线调制解调器**：DOCSIS

## 自适应调制

现代通信系统会根据信道质量动态调整调制方式：

| SNR条件 | 调制方式 | 数据速率 |
|---------|----------|----------|
| 很差    | BPSK     | 1x       |
| 较差    | QPSK     | 2x       |
| 一般    | 16-QAM   | 4x       |
| 良好    | 64-QAM   | 6x       |
| 很好    | 256-QAM  | 8x       |

## 参考资料

1. Proakis, J. G. (2008). *Digital Communications* (5th ed.). McGraw-Hill.
2. [Wikipedia - QAM](https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation)
3. 3GPP TS 36.211 - Physical channels and modulation (LTE)
