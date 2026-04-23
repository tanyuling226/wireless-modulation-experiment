# Git 快速入门

本指南帮助你快速掌握实验所需的 Git 基本操作。

---

## 什么是 Git？

Git 是一个版本控制系统，用于：
- 跟踪代码的修改历史
- 多人协作开发
- 备份和恢复代码

GitHub 是基于 Git 的代码托管平台。

---

## 实验工作流程

```
1. Fork模板仓库到你的GitHub账号
   ↓
2. Clone到本地
   ↓
3. 编写代码
   ↓
4. Commit提交修改
   ↓
5. Push到GitHub
   ↓
6. 创建Pull Request
   ↓
7. 自动评分
```

---

## 1. Fork 仓库

在 GitHub 网页上：

1. 访问教师提供的模板仓库
2. 点击右上角的 **Fork** 按钮
3. 仓库会复制到你的账号下

---

## 2. Clone 到本地

打开终端（或 Git Bash），运行：

```bash
git clone https://github.com/你的用户名/wireless-modulation-experiment.git
cd wireless-modulation-experiment
```

---

## 3. 基本 Git 命令

### 查看状态

```bash
git status
```

显示哪些文件被修改、新增或删除。

### 添加文件到暂存区

```bash
# 添加单个文件
git add src/modulation.py

# 添加所有修改
git add .

# 添加results目录下的所有文件
git add results/
```

### 提交修改

```bash
git commit -m "完成BPSK调制实现"
```

**提交信息规范**：
- 简洁明了，说明做了什么
- 使用中文或英文均可
- 示例：
  - ✅ "实现BPSK和QPSK调制"
  - ✅ "修复星座图显示问题"
  - ✅ "添加实验报告"
  - ❌ "update"
  - ❌ "修改"

### 推送到 GitHub

```bash
git push origin main
```

如果是第一次推送，可能需要：

```bash
git push -u origin main
```

---

## 4. 常用场景

### 场景1: 第一次提交

```bash
# 1. 修改了文件后，查看状态
git status

# 2. 添加所有修改
git add .

# 3. 提交
git commit -m "完成BPSK和QPSK实现"

# 4. 推送
git push origin main
```

### 场景2: 增量提交

```bash
# 修改代码...
git add src/modulation.py results/
git commit -m "完成16-QAM调制"
git push origin main
```

### 场景3: 查看修改历史

```bash
# 查看提交日志
git log

# 简洁版
git log --oneline

# 查看最近3条
git log -n 3
```

### 场景4: 查看文件差异

```bash
# 查看未暂存的修改
git diff

# 查看已暂存的修改
git diff --staged

# 查看特定文件的修改
git diff src/modulation.py
```

---

## 5. 创建 Pull Request

### 步骤1: 确保代码已推送

```bash
git push origin main
```

### 步骤2: 在 GitHub 网页上创建 PR

1. 访问你的仓库（`https://github.com/你的用户名/wireless-modulation-experiment`）
2. 点击 **Pull requests** 标签
3. 点击 **New pull request**
4. 选择：
   - Base repository: `教师的仓库`
   - Base branch: `main`
   - Head repository: `你的仓库`
   - Compare branch: `main`
5. 填写 PR 标题和描述：

**标题示例**：
```
[学号] 姓名 - 数字调制解调实验提交
```

**描述示例**：
```
## 完成情况

- [x] 任务0: 环境配置
- [x] 任务1: BPSK调制
- [x] 任务2: QPSK调制
- [x] 任务3: 16-QAM调制
- [ ] 任务4: 解调实现（选做）
- [ ] 任务5: BER性能分析（选做）
- [x] 任务6: 实验报告

## 说明

所有必做任务已完成，星座图正确生成。
使用GitHub Copilot辅助编程。
```

6. 点击 **Create pull request**

---

## 6. 自动评分流程

创建 PR 后：

1. **GitHub Actions 自动运行**（3-5分钟）
2. **评分结果显示在 PR 评论中**
3. **查看详细日志**：
   - 点击 PR 页面的 **Checks** 标签
   - 点击 **自动评分系统**
   - 展开各个步骤查看详情

如果测试未通过：
- 根据错误信息修改代码
- 重新 commit 并 push
- GitHub Actions 会自动重新评分

---

## 7. 常见问题

### Q1: 忘记添加文件就 commit 了？

```bash
# 添加遗漏的文件
git add 遗漏的文件

# 修正上一次提交（不产生新的commit）
git commit --amend --no-edit
```

### Q2: 提交信息写错了？

```bash
# 修改最后一次提交的信息
git commit --amend -m "正确的提交信息"
```

### Q3: 想撤销某个文件的修改？

```bash
# 撤销对文件的修改（恢复到上次commit的状态）
git checkout -- src/modulation.py

# 或者使用新语法
git restore src/modulation.py
```

### Q4: 想撤销已经 add 的文件？

```bash
# 从暂存区移除，但保留修改
git reset HEAD src/modulation.py

# 或者使用新语法
git restore --staged src/modulation.py
```

### Q5: 推送失败，提示 "rejected"？

可能是远程仓库有更新，需要先拉取：

```bash
# 拉取远程更新
git pull origin main

# 如果有冲突，解决后再提交
git add .
git commit -m "解决冲突"
git push origin main
```

### Q6: 如何查看远程仓库地址？

```bash
git remote -v
```

---

## 8. .gitignore 文件

`.gitignore` 用于忽略不需要提交的文件，例如：

```
# Python
__pycache__/
*.pyc

# 结果文件（可选：如果想提交results，删除这一行）
results/

# IDE
.vscode/
.idea/

# OS
.DS_Store
```

本实验已配置好 `.gitignore`，无需修改。

---

## 9. Git 图形化工具

如果不喜欢命令行，可以使用图形化工具：

### VS Code 内置 Git

1. 点击左侧的 **Source Control** 图标
2. 查看修改的文件
3. 点击 `+` 添加到暂存区
4. 输入提交信息并点击 ✓ 提交
5. 点击 `...` → `Push` 推送

### GitHub Desktop

下载：https://desktop.github.com/

提供友好的图形界面，适合初学者。

---

## 10. 参考资料

- [Git 官方文档](https://git-scm.com/doc)
- [GitHub 官方教程](https://docs.github.com/cn/get-started)
- [Git 速查表](https://education.github.com/git-cheat-sheet-education.pdf)

---

## 11. 实验专用速查表

```bash
# 克隆仓库
git clone https://github.com/你的用户名/wireless-modulation-experiment.git

# 查看状态
git status

# 添加所有修改
git add .

# 提交
git commit -m "完成BPSK和QPSK"

# 推送
git push origin main

# 查看提交历史
git log --oneline

# 查看修改
git diff
```

---

**如有疑问，请向教师或助教求助！** 🚀
