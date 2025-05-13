# SQL注入工具

>

---

## 项目结构

本项目由 `Python` 语言编写，采用如下结构：

`ui`：窗口设计文件

`controller`：界面事件处理

`service`：业务逻辑处理

`sqlmap`：sqlmap工具

---

## 运行

### 使用 PyCharm

本项目是用 **PyCharm** 写的，可以通过 **PyCharm** 打开。直接点击右上角的绿色箭头运行即可。

### 使用命令行

直接在项目根目录下运行：

```bash
python main.py
```

---

## 构建

直接在项目根目录下运行：

```bash
python setup.py build
```

构建出来的 `exe` 文件可以在 `build` 目录下找到。如 `build/exe.win-amd64-3.11/main.exe` 。

然后可以通过 `Enigma Virtual Box` 等打包工具打包成单个 `exe` 文件。

---