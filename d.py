import ctypes

from PySide6.QtWidgets import QPushButton, QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 启用鼠标追踪
        button = QPushButton("Run as administrator")
        button.clicked.connect(self.run)
        self.setCentralWidget(button)

    def run(self):
        # 定义子程序的路径
        sub_program = r"E:\imageWord\dist\e.exe"

        # 使用ShellExecute函数以管理员权限运行子程序
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sub_program, None, None, 1)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()