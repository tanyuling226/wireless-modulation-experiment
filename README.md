# 数字调制解调实验

## 📚 实验概述

本实验要求学生实现常见的数字调制方式（BPSK、QPSK、16-QAM），生成星座图，并选做性能分析。实验使用 Python + NumPy + Matplotlib，鼓励使用 AI 编程助手（GitHub Copilot / Claude Code）。

**实验时长**：2小时（120分钟）
- 第一小时：教师讲解和演示
- 第二小时：学生动手实验

**提交截止**：实验课后7天（下周四 23:59）

---

## 🎯 实验目标

1. 理解数字调制的基本原理（BPSK、QPSK、16-QAM）
2. 实现调制算法并可视化星座图
3. 学习使用 AI 编程助手辅助开发
4. 熟悉 GitHub 协作流程和自动评分系统

---

## 📝 实验任务

### 任务0：环境准备（5分）
- 使用 Copilot Agent 配置 Python 环境
- Fork 本仓库到个人账号
- Clone 到本地并安装依赖

### 任务1：BPSK 调制（25分）✅ 必做
在 `src/modulation.py` 中实现 `bpsk_modulate()` 函数：
- 输入：比特序列 `[0, 1, 0, 1, ...]`
- 输出：符号序列 `[+1, -1, +1, -1, ...]`
- 映射关系：`0 → +1`, `1 → -1`
- 生成星座图并保存到 `results/bpsk_constellation.png`

### 任务2：QPSK 调制（25分）✅ 必做
在 `src/modulation.py` 中实现 `qpsk_modulate()` 函数：
- 每2比特一组
- 格雷码映射：
  - `00 → (1+1j)/√2` (45°)
  - `01 → (-1+1j)/√2` (135°)
  - `11 → (-1-1j)/√2` (225°)
  - `10 → (1-1j)/√2` (315°)
- 生成星座图并保存到 `results/qpsk_constellation.png`

### 任务3：16-QAM 调制（20分）✅ 必做
在 `src/modulation.py` 中实现 `qam16_modulate()` 函数：
- 每4比特一组
- I/Q 分量取值：`-3, -1, +1, +3`
- 生成16个符号的星座图
- 保存到 `results/16qam_constellation.png`

### 任务4：解调实现（10分）⭐ 选做
在 `src/demodulation.py` 中实现解调函数：
- `bpsk_demodulate()`：判决准则
- `qpsk_demodulate()`：最小欧氏距离判决
- `qam16_demodulate()`：最小欧氏距离判决

### 任务5：BER 性能分析（10分）⭐ 选做
在 `src/performance_test.py` 中完成性能测试：
- 生成随机比特序列
- 调制 → 添加 AWGN 噪声 → 解调
- 扫描不同 SNR（0~15 dB）
- 绘制 BER vs SNR 曲线（对数坐标）

### 任务6：实验报告（15分）📄 可课后完成
在根目录创建 `REPORT.md`，包含：
1. 实验目的
2. 实验原理（简述BPSK/QPSK/QAM）
3. 实验方法与步骤
4. 实验结果（插入星座图）
5. 结果分析与讨论
6. 实验心得与 Copilot 使用体会
7. 参考文献

⚠️ **重要**：实验结果（代码+星座图）必须提交，实验报告可以后续完善。

---

## 🚀 快速开始

### 1. 环境配置（第一小时）

**使用 Copilot Agent 自动配置**（推荐）：
```
打开 VSCode Copilot Chat，输入：
"请帮我配置 Python 开发环境，需要安装 numpy、scipy、matplotlib"
```

**手动安装**（备选）：
```bash
# 1. 安装 Python 3.8+
# 2. 安装依赖
pip install -r requirements.txt
```

### 2. 获取实验代码

```bash
# Fork 本仓库到你的 GitHub 账号
# 然后 Clone 到本地
git clone https://github.com/你的用户名/wireless-modulation-experiment.git
cd wireless-modulation-experiment

# 测试环境
python src/test_environment.py
```

### 3. 完成实验

打开 `src/modulation.py`，使用 GitHub Copilot 辅助完成代码：

**提示词示例**：
```
"请实现 BPSK 调制函数，输入是比特序列，输出是符号序列，
其中比特0映射到+1，比特1映射到-1"
```

运行测试：
```bash
python src/modulation.py
```

检查结果：
- 查看 `results/` 目录是否生成了星座图
- 确认图片清晰、坐标轴标注正确

### 4. 提交到 GitHub

```bash
git add .
git commit -m "完成 BPSK 和 QPSK 调制"
git push origin main
```

在 GitHub 网页上创建 Pull Request：
1. 访问你的仓库
2. 点击 "Pull requests" → "New pull request"
3. 填写 PR 描述（说明完成了哪些任务）
4. 点击 "Create pull request"

### 5. 查看自动评分

等待 3-5 分钟，GitHub Actions 会自动运行评分脚本。
评分结果会以 Comment 形式显示在你的 PR 下方。

---

## 💡 使用 AI 助手的提示

### 推荐的提问模板

**调制实现**：
```
"请用 Python 实现 BPSK 调制，输入二进制序列，
输出复数符号序列，0映射到+1，1映射到-1"
```

**星座图绘制**：
```
"请用 matplotlib 画出 QPSK 的星座图，
四个点在单位圆上均匀分布"
```

**代码调试**：
```
"我的代码报错了：[粘贴错误信息]，请帮我找出问题"
```

**代码解释**：
```
"请解释这段代码的含义：[粘贴代码]"
```

### AI 助手使用建议

✅ 先理解原理，再使用 AI 生成代码  
✅ 生成的代码要仔细阅读理解  
✅ 可以让 AI 解释代码的实现逻辑  
✅ 遇到错误时，将完整错误信息粘贴给 AI  
✅ 尝试修改参数观察结果变化  

❌ 不要完全依赖 AI，要培养独立思考能力  
❌ 不要直接提交 AI 生成的代码而不理解其含义  

---

## 📊 评分标准

| 评分项 | 分值 | 评分细则 |
|--------|------|----------|
| 环境配置 | 5分 | 成功运行环境测试脚本 |
| BPSK调制 | 25分 | 映射正确(15分) + 星座图(10分) |
| QPSK调制 | 25分 | 映射正确(15分) + 星座图(10分) |
| 16-QAM调制 | 20分 | 映射正确(12分) + 星座图(8分) |
| 解调实现 | 10分 | 正确实现解调算法（选做加分） |
| BER性能 | 10分 | 生成BER曲线并分析（选做加分） |
| 实验报告 | 15分 | 完整性(8分) + 分析深度(7分) |
| 代码质量 | -10~+5分 | pylint评分 > 8.0加分，< 5.0扣分 |

**总分**：基础任务（0-3+报告）满分75分，选做任务可额外加分20分。

---

## 📁 仓库结构

```
wireless-modulation-experiment/
├── README.md                    # 本文件
├── REQUIREMENTS.md              # 详细任务要求
├── .github/workflows/
│   └── grading.yml              # 自动评分工作流
├── docs/
│   ├── theory_bpsk.md           # BPSK原理
│   ├── theory_qpsk.md           # QPSK原理
│   ├── theory_qam.md            # QAM原理
│   └── copilot_guide.md         # Copilot使用指南
├── src/
│   ├── modulation.py            # 调制函数（学生填充）
│   ├── demodulation.py          # 解调函数（学生填充）
│   ├── performance_test.py      # 性能测试（学生填充）
│   ├── utils.py                 # 工具函数（已实现）
│   └── test_environment.py      # 环境测试脚本
├── grading/                     # 评分脚本（学生不可见）
│   ├── test_bpsk.py
│   ├── test_qpsk.py
│   ├── test_qam16.py
│   ├── check_report.py
│   └── calculate_grade.py
├── examples/                    # 示例输出
│   ├── bpsk_constellation.png
│   ├── qpsk_constellation.png
│   └── ber_curve_example.png
├── results/                     # 学生结果（自动创建）
├── requirements.txt             # Python依赖
├── .gitignore
└── REPORT_TEMPLATE.md           # 报告模板
```

---

## ❓ 常见问题

**Q1: 我不会用 Git，怎么办？**  
A: 课上会有 10 分钟的 Git 快速演示，也可以查看 [Git 快速入门](docs/git_quickstart.md)。

**Q2: GitHub Copilot 需要付费吗？**  
A: 学生可以申请免费使用，访问 https://education.github.com/ 申请。

**Q3: 我的代码运行报错，怎么办？**  
A: 将完整错误信息粘贴给 Copilot 求助，或向教师/助教求助。

**Q4: 星座图应该是什么样的？**  
A: 查看 `examples/` 目录中的示例图片。

**Q5: 我可以多次提交吗？**  
A: 可以！在截止时间前可以随意修改和提交，系统会取最后一次评分。

**Q6: 选做任务必须做吗？**  
A: 不是必须的。基础任务满分75分即可及格，选做任务是加分项。

---

## 📖 参考资料

- [BPSK原理详解](docs/theory_bpsk.md)
- [QPSK原理详解](docs/theory_qpsk.md)
- [QAM原理详解](docs/theory_qam.md)
- [GitHub Copilot 使用指南](docs/copilot_guide.md)
- [Git 快速入门](docs/git_quickstart.md)

---

## 📧 联系方式

如有问题，请通过以下方式联系：
- 课程群：[课程群号]
- 邮箱：[教师邮箱]
- Office Hours：[时间地点]

---

**祝实验顺利！🎉**
