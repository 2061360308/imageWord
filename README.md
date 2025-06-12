# 安建排图

一个用于图片排版的桌面应用程序，支持多种布局模板和自定义设置。

## 功能特性

- 📐 多种预设布局模板（1-3行，1-3列组合）
- 🔄 支持横版和竖版页面方向
- 📄 A4纸张规格，可自定义页边距
- 🖱️ 右键菜单集成，方便快捷操作
- ⚙️ 用户配置数据持久化存储

## 系统要求

- Windows 操作系统
- Python 3.7+
- PySide6

## 安装使用

### 直接运行（开发环境）

1. 克隆项目到本地
```bash
git clone <repository-url>
cd imageWord
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行程序
```bash
python main.py
```

### 构建可执行文件

使用提供的构建脚本：

```bash
cd buildTools
build.bat
```

构建过程包括：
1. 构建 registerMenu 组件
2. 构建 layoutImage 组件  
3. 生成资源文件
4. 构建主程序

## 项目结构

```
imageWord/
├── buildTools/                 # 构建工具
│   └── build.bat               # 构建脚本
├── spec/                       # PyInstaller 配置文件
│   ├── registerMenu.spec       # 右键菜单注册程序配置
│   ├── layoutImage.spec        # 图片布局程序配置
│   └── 安建排图.spec           # 主程序配置
├── UI/                         # 用户界面模块
├── module/                     # 功能模块
├── res/                        # 资源文件
├── buildRes.py                 # 资源构建脚本
├── userData.py                 # 用户数据管理
├── documentCreator.py          # 文档创建功能
├── imgTempMemory.py            # 图片临时内存管理
├── registerMenu.py             # 右键菜单注册
├── layoutImage.py              # 图片布局处理
├── main.py                     # 主程序入口
├── requirements.txt            # 依赖包列表
├── .gitignore                  # Git忽略文件配置
├── LICENSE                     # 许可证文件
└── README.md                   # 项目说明文档
```

## 配置说明

程序首次运行时会在用户目录下创建配置文件夹：
```
%APPDATA%/安建排图/
├── template.json        # 模板配置文件
├── layoutImage.exe      # 图片布局程序
└── registerMenu.exe     # 右键菜单注册程序
```

### 默认模板

程序预设6种基础布局模板：
- 一行一列、一行两列、一行三列
- 两行一列、两行两列、两行三列

每种模板支持横版和竖版两个方向，共计12个模板选项。

## 开发说明

- 使用 PySide6 构建GUI界面
- PyInstaller 用于打包可执行文件
- 支持Windows右键菜单集成
- 配置文件使用JSON格式存储

## 许可证

[MIT 许可授权](./LICENSE)

## 贡献

欢迎提交Issue和Pull Request！