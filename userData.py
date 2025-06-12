# 用户数据
import os.path
rootPath = os.path.join(os.path.expanduser('~'), "AppData", "Roaming", "安建排图")


def firstRunCheck():
    # 检查是否第一次运行
    print("检查是否第一次运行")
    if not os.path.exists(rootPath):

        from PySide6 import QtCore
        from PySide6.QtCore import QIODevice
        import ctypes
        import resources_rc

        # 首次运行写出资源
        os.makedirs(rootPath)

        # 写出exe
        file = QtCore.QFile(u':/app/dist/layoutImage.exe')
        if not file.open(QIODevice.ReadOnly):
            print("打开失败")
        # file.open(QIODevice.ReadOnly)
        data = file.readAll()
        with open(os.path.join(rootPath, "layoutImage.exe"), 'wb') as f:
            f.write(data.data())

        file = QtCore.QFile(u':/app/dist/registerMenu.exe')
        if not file.open(QIODevice.ReadOnly):
            print("打开失败")
        # file.open(QIODevice.ReadOnly)
        data = file.readAll()
        with open(os.path.join(rootPath, "registerMenu.exe"), 'wb') as f:
            f.write(data.data())

        sub_program = os.path.join(rootPath, "registerMenu.exe")
        args = '"1 1 0"'
        # 注册右击菜单
        # 使用ShellExecute函数以管理员权限运行子程序
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sub_program, args, None, 1)

        # 写出模板文件
        setDefaultTemplate()


def setDefaultTemplate():
    import json
    # 预设模板
    default_page_size = (21, 29.7)  # A4纸大小, 单位cm
    default_page_margin = (0.5, 0.5, 0.5, 0.5)  # 页边距，上下左右, 单位cm
    default_template = [{"name": "一行一列", "icon": "一行一列", "arrangement": (1, 1)},
                        {"name": "一行两列", "icon": "一行两列", "arrangement": (1, 2)},
                        {"name": "一行三列", "icon": "一行三列", "arrangement": (1, 3)},
                        {"name": "两行一列", "icon": "两行一列", "arrangement": (2, 1)},
                        {"name": "两行两列", "icon": "两行两列", "arrangement": (2, 2)},
                        {"name": "两行三列", "icon": "两行三列", "arrangement": (2, 3)},
                        ]
    template = []
    for index, default in enumerate(default_template):
        item = dict(default)
        item["size"] = default_page_size
        item["margin"] = default_page_margin
        item["direction"] = 0
        item["index"] = index
        template.append(item)
    for index, default in enumerate(default_template):
        item = dict(default)
        size = (default_page_size[1], default_page_size[0])
        item["size"] = size
        item["margin"] = default_page_margin
        item["direction"] = 1
        item["index"] = index + len(default_template)
        template.append(item)
    
    with open(os.path.join(rootPath, "template.json"), "w+") as f:
        print("写出模板文件")
        # print(template)
        f.write(json.dumps(template))


def getTemplate():
    import json
    """
    获取模板数据
    :return:
    """
    try:
        with open(os.path.join(rootPath, "template.json"), "r") as f:
            return json.loads(f.read())
    except FileNotFoundError or json.JSONDecodeError:
        print("模板文件不存在或者格式错误，已重置模板文件")
        setDefaultTemplate()
        with open(os.path.join(rootPath, "template.json"), "r") as f:
            return json.loads(f.read())
