from os.path import join, expanduser
from sys import argv
from winreg import OpenKey, CreateKey, SetValueEx, CloseKey, HKEY_CLASSES_ROOT, KEY_SET_VALUE, REG_SZ

rootPath = join(expanduser('~'), "AppData", "Roaming", "安建排图")

command = argv[1]

# 定义你的程序的路径
program_path = join(rootPath, "layoutImage.exe")

# 打开注册表的键
key = OpenKey(HKEY_CLASSES_ROOT, r"Directory\shell", 0, KEY_SET_VALUE)

# 创建一个新的键，这个键的名字就是你的右键菜单的名字
sub_key = CreateKey(key, "安建排图")

# 在新的键下创建一个名为"command"的键，这个键的默认值就是你的程序的路径
command_key = CreateKey(sub_key, "command")
SetValueEx(command_key, "", 0, REG_SZ, f"{program_path} %1 {command}")

# 关闭所有的键
CloseKey(command_key)
CloseKey(sub_key)
CloseKey(key)
