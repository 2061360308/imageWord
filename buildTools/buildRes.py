import codecs
import re
import os

originPath = "./designer_ui"
targetPath = "./UI"


def gender_ui_py(file_path):
    """
    生成ui文件对应的py文件
    :return:
    """
    target = os.path.join(targetPath, os.path.basename(file_path).split('.')[0]) + '.py'

    # 生成py文件
    os.system('pyside6-uic -o %s %s' % (target, file_path))
    print("执行：" + 'pyside6-uic -o %s %s' % (target, file_path))

    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换u""字符串
    print("【】【】【】替换u\"\"字符串")
    content = replace_unicode_strings(content)
    print("【】【】【】更改类结构")
    content = reconfiguration(content)

    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)


def replace_unicode_strings(content):
    # 查找所有的 u"" 字符串
    content = re.sub(r'u"(.*?)"', lambda m: decode(m.group(0)), content)

    return content


def decode(unistr):
    decoded_string = re.sub(r'\\u[0-9a-fA-F]{4}', lambda m: codecs.decode(m.group(0), 'unicode_escape'), unistr)
    return decoded_string


def getClassName(function_definition):
    match = re.search(r'def setupUi\(self, (\w+)\)', function_definition)
    if match:
        return match.group(1)


def reconfiguration(content):
    className = getClassName(content)
    print("* * * * ** className: " + className)
    # 更改类结构
    content = content.replace(className + ".", "self.")
    content = content.replace(f", {className})", ")")
    content = content.replace(f"({className})", "(self)")
    content = content.replace("self.retranslateUi(self)", "self.retranslateUi()")

    return content


if __name__ == '__main__':
    # 获取源文件夹下的所有ui文件
    file_list = os.listdir(originPath)
    for file in file_list:
        print(file)
        if file.endswith('.ui'):
            gender_ui_py(os.path.join(originPath, file))

    print("【】【】【】编译资源文件")
    
    # 获取当前文件夹的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    output_path = os.path.join(current_dir, "../resources_rc.py")
    qrc_file= os.path.join(current_dir, "./resources.qrc")
    
    print(f"编译资源文件到: {output_path}")
    print(f"资源文件路径: {qrc_file}")
    
    
    # 编译资源文件
    os.system(f'pyside6-rcc -o { output_path } { qrc_file } ')
