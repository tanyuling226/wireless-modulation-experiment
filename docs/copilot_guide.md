# GitHub Copilot 使用指南

本指南帮助你在数字调制解调实验中有效使用 GitHub Copilot 和其他 AI 编程助手。

---

## 1. 什么是 GitHub Copilot？

GitHub Copilot 是一个 AI 编程助手，可以：
- 根据注释自动生成代码
- 补全函数和代码块
- 提供多个实现方案供选择
- 解释现有代码
- 帮助调试错误

---

## 2. 如何获取 GitHub Copilot？

### 学生免费使用

1. 访问 [GitHub Education](https://education.github.com/)
2. 使用学校邮箱申请 GitHub Student Developer Pack
3. 审核通过后，Copilot 将自动激活

### 安装 VS Code 扩展

1. 打开 VS Code
2. 在扩展市场搜索 "GitHub Copilot"
3. 安装并登录你的 GitHub 账号

---

## 3. 基本使用技巧

### 3.1 通过注释引导生成代码

**✅ 好的提示（详细且明确）**：

```python
def bpsk_modulate(bits):
    """
    BPSK调制函数
    将二进制比特序列映射到符号序列
    0 -> +1, 1 -> -1
    返回复数数组
    """
    # [Copilot会在这里生成代码]
```

**❌ 不好的提示（过于简略）**：

```python
def bpsk_modulate(bits):
    # 实现BPSK
```

### 3.2 分步引导

将复杂任务分解成小步骤：

```python
def qpsk_modulate(bits):
    # 步骤1: 检查输入长度是否为偶数
    
    # 步骤2: 将比特序列reshape成(N/2, 2)
    
    # 步骤3: 对每对比特应用格雷码映射
    
    # 步骤4: 归一化到单位功率
    
    return symbols
```

Copilot 会逐步生成每个部分的代码。

### 3.3 使用示例数据

提供示例输入输出：

```python
def qpsk_modulate(bits):
    """
    示例:
        输入: [0, 0, 0, 1, 1, 1, 1, 0]
        输出: [(1+1j)/√2, (-1+1j)/√2, (-1-1j)/√2, (1-1j)/√2]
    """
    # Copilot会根据示例生成代码
```

---

## 4. 实验中的具体应用

### 任务1: 实现BPSK调制

**推荐提示词**：

```python
def bpsk_modulate(bits):
    """
    实现BPSK调制
    
    参数:
        bits: numpy数组，元素为0或1
    
    返回:
        symbols: numpy复数数组
        - 比特0映射到+1
        - 比特1映射到-1
    
    实现提示:
        使用numpy的向量化操作，避免循环
    """
```

### 任务2: 绘制星座图

**推荐提示词**：

```python
def plot_constellation(symbols, title):
    """
    绘制星座图
    
    参数:
        symbols: 复数符号数组
        title: 图表标题
    
    要求:
        - 使用matplotlib绘制散点图
        - 显示实部和虚部坐标轴
        - 添加网格
        - 保存到results/目录
    """
```

### 任务3: 添加AWGN噪声

**推荐提示词**：

```python
def add_awgn(signal, snr_db):
    """
    向信号添加加性高斯白噪声
    
    参数:
        signal: 复数信号数组
        snr_db: 信噪比（分贝）
    
    返回:
        noisy_signal: 加噪后的信号
    
    实现步骤:
        1. 计算信号功率
        2. 根据SNR计算噪声功率
        3. 生成复高斯噪声（实部和虚部独立）
        4. 将噪声加到信号上
    """
```

---

## 5. 调试技巧

### 5.1 让 Copilot 解释错误

当代码报错时，选中错误信息和相关代码，然后：

1. 打开 Copilot Chat (Ctrl+I 或 Cmd+I)
2. 输入：

```
我的代码报错了：
[粘贴错误信息]

请帮我找出问题并建议修改方案。
```

### 5.2 验证生成的代码

Copilot 生成代码后，务必：

1. **阅读并理解**：确保代码逻辑正确
2. **运行测试**：验证输出是否符合预期
3. **检查边界条件**：输入异常值测试

### 5.3 对比多个方案

在函数内按 `Alt+]` (或 `Cmd+]`) 查看 Copilot 提供的其他实现方案，选择最优的。

---

## 6. 高级技巧

### 6.1 使用 Copilot Chat

打开 Chat 面板进行对话式编程：

```
提示: 请帮我实现QPSK调制，要求使用格雷码映射，
并将符号归一化到单位能量。

Copilot: [生成代码并解释]

你: 能否添加输入验证，检查比特数组长度是否为偶数？

Copilot: [更新代码]
```

### 6.2 代码重构

选中一段代码，在 Chat 中输入：

```
请优化这段代码，提高可读性和性能。
```

### 6.3 生成测试用例

```python
# 输入：请为bpsk_modulate函数生成完整的pytest测试用例

# Copilot会生成：
def test_bpsk_modulate():
    # 测试基本映射
    bits = np.array([0, 1, 0, 1])
    symbols = bpsk_modulate(bits)
    expected = np.array([1, -1, 1, -1])
    assert np.allclose(symbols, expected)
    
    # 测试全0
    ...
```

---

## 7. 注意事项

### ⚠️ 不要完全依赖 AI

- **理解原理**：先学习调制原理，再使用 Copilot
- **独立思考**：AI 生成的代码可能有错，需要人工审查
- **学习为主**：Copilot 是辅助工具，不是替代思考

### ⚠️ 避免学术不诚信

- 使用 Copilot 辅助编程是**允许的**
- 但必须**理解并能解释**所有提交的代码
- 在报告中**注明**使用了 AI 助手

### ⚠️ 代码质量检查

Copilot 生成的代码可能：
- 缺少错误处理
- 效率不是最优
- 不符合代码规范

提交前务必：
- 运行 `pylint` 检查代码质量
- 运行所有测试用例
- 手动 review 关键逻辑

---

## 8. 常见问题

### Q1: Copilot 生成的代码不正确怎么办？

A: 
1. 检查提示词是否足够详细
2. 尝试分步引导
3. 查看其他建议（Alt+]）
4. 手动修改并学习正确实现

### Q2: Copilot 没有反应？

A:
1. 确认已登录 GitHub 账号
2. 检查网络连接
3. 重启 VS Code
4. 查看扩展是否已启用

### Q3: 如何提高 Copilot 的准确率？

A:
- 编写详细的函数文档
- 提供示例输入输出
- 使用清晰的变量命名
- 保持代码上下文简洁

---

## 9. 替代方案

如果无法使用 GitHub Copilot，可以尝试：

### 9.1 Claude / ChatGPT

在网页中与 AI 对话：

```
你: 请帮我用Python实现BPSK调制函数，
输入是numpy数组[0,1,0,1]，输出应该是[1,-1,1,-1]

AI: [生成代码]

你: 如何绘制星座图？

AI: [提供matplotlib代码]
```

### 9.2 本地 Copilot Agent

在 VS Code 中使用 Copilot Agent（需要付费）：

```
@workspace 帮我配置Python环境并安装numpy、matplotlib
```

### 9.3 其他 AI 编码助手

- **Cursor**：AI-first 编辑器
- **Tabnine**：代码补全工具
- **Amazon CodeWhisperer**：AWS 的 AI 编程助手

---

## 10. 实验报告中如何写使用体会？

在报告的"实验心得"部分，可以这样写：

**示例1**（简洁版）：

> 在本实验中，我使用了 GitHub Copilot 辅助编程。Copilot 在实现基础映射逻辑时提供了很大帮助，但在归一化和格雷码映射部分，我需要根据理论知识手动调整。总体而言，AI 助手可以提高编程效率，但理解原理仍然是最重要的。

**示例2**（详细版）：

> **AI 助手使用情况**
> 
> 本实验中使用了 GitHub Copilot 进行辅助编程，主要体会如下：
> 
> 1. **有帮助的场景**：
>    - 生成NumPy数组操作的样板代码
>    - 快速实现matplotlib绘图框架
>    - 自动补全函数参数和类型提示
> 
> 2. **需要人工修正的场景**：
>    - QPSK格雷码映射的具体实现
>    - 16-QAM归一化因子的计算
>    - 边界条件的错误处理
> 
> 3. **学习收获**：
>    - 学会了如何有效地与AI协作
>    - 理解了提示工程（Prompt Engineering）的重要性
>    - 体会到AI是工具而非替代，扎实的理论基础仍然必不可少

---

## 11. 总结

GitHub Copilot 是强大的辅助工具，但：

✅ **应该**：
- 用于加速编程流程
- 生成样板代码
- 探索不同实现方案
- 学习新的API用法

❌ **不应该**：
- 完全依赖而不理解原理
- 不加审查地提交生成的代码
- 把AI当作"作业代写工具"

记住：**AI是助手，你才是工程师！** 🚀

---

**祝实验顺利！如有问题，请随时向教师或助教求助。**
