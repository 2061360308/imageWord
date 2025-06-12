import os

from documentCreator import DocumentCreator, ImageZoom
from imgTempMemory import imgTempMemory
from userData import firstRunCheck

firstRunCheck()  # 首次运行检查

from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QPushButton, QStatusBar, QFileDialog, QInputDialog
from PySide6.QtGui import QPixmap, QAction, QActionGroup
from PySide6.QtCore import QSize
from qt_material import apply_stylesheet
from UI import Ui_MainWindow
from template import template
from globalVar import globalVar
from module.PicPreviewArea import Status as PicPreviewAreaStatus


class StatusBar(QStatusBar):
    loss_rate = 1

    def __init__(self, parent=None):
        super().__init__(parent)

        self.col1 = QPushButton()
        self.col1.setIcon(QPixmap(u":/icon/res/icon/16gl-1.png"))
        self.col1.setFixedSize(16, 16)
        self.col1.setFlat(True)
        self.col1.clicked.connect(lambda: self.colButtonClicked(1))
        self.col1.setToolTip("单列显示")
        self.col2 = QPushButton()
        self.col2.setIcon(QPixmap(u":/icon/res/icon/16gl-2.png"))
        self.col2.setFixedSize(16, 16)
        self.col2.setFlat(True)
        self.col2.clicked.connect(lambda: self.colButtonClicked(2))
        self.col2.setToolTip("双列显示")
        self.col3 = QPushButton()
        self.col3.setIcon(QPixmap(u":/icon/res/icon/16gl-3.png"))
        self.col3.setFixedSize(16, 16)
        self.col3.setFlat(True)
        self.col3.clicked.connect(lambda: self.colButtonClicked(3))
        self.col3.setToolTip("三列显示")
        self.col4 = QPushButton()
        self.col4.setIcon(QPixmap(u":/icon/res/icon/16gl-4.png"))
        self.col4.setFixedSize(16, 16)
        self.col4.setFlat(True)
        self.col4.clicked.connect(lambda: self.colButtonClicked(4))
        self.col4.setToolTip("四列显示")

        self.filterMenu = QMenu()
        self.filterMenu.setStyleSheet("QMenu::item:checked { background-color: rgba(18, 150, 219, 50); }")
        self.filterButton = QPushButton("筛选")
        self.filterButton.setIcon(QPixmap(u":/icon/res/icon/筛选.png"))
        # self.filterButton.setFixedSize(100, 20)
        self.filterButton.setFixedHeight(20)
        self.filterButton.setFlat(True)
        self.filterButton.setMenu(self.filterMenu)

        # 创建菜单项
        self.directionAction = QAction("图片方向不符", self)
        self.directionAction.setIcon(QPixmap(u":/icon/res/icon/ass-unassigned.png"))
        self.directionAction.setCheckable(True)
        self.lossMenu = QMenu(self)
        self.lossMenu.setTitle("页面损失率")
        self.lossMenu.setIcon(QPixmap(u":/icon/res/icon/rate-down_finance_line.png"))
        self.loss20Action = QAction("20%")
        self.loss20Action.setCheckable(True)
        self.loss30Action = QAction("30%")
        self.loss30Action.setCheckable(True)
        self.loss40Action = QAction("40%")
        self.loss40Action.setCheckable(True)
        self.loss50Action = QAction("50%")
        self.loss50Action.setCheckable(True)
        self.loss60Action = QAction("60%")
        self.loss60Action.setCheckable(True)
        self.lossCustom = QAction("自定义")
        self.lossCustom.setCheckable(True)
        self.lossMenu.addAction(self.loss20Action)
        self.lossMenu.addAction(self.loss30Action)
        self.lossMenu.addAction(self.loss40Action)
        self.lossMenu.addAction(self.loss50Action)
        self.lossMenu.addAction(self.loss60Action)
        self.lossMenu.addAction(self.lossCustom)
        self.clearAction = QAction("清除筛选", self)
        self.clearAction.setCheckable(True)
        self.clearAction.setChecked(True)

        # 创建动作组
        self.actionGroup = QActionGroup(self)
        self.actionGroup.addAction(self.directionAction)
        self.actionGroup.addAction(self.loss20Action)
        self.actionGroup.addAction(self.loss30Action)
        self.actionGroup.addAction(self.loss40Action)
        self.actionGroup.addAction(self.loss50Action)
        self.actionGroup.addAction(self.loss60Action)
        self.actionGroup.addAction(self.lossCustom)
        self.actionGroup.addAction(self.clearAction)

        # 添加菜单项，动作到菜单
        self.filterMenu.addMenu(self.lossMenu)
        self.filterMenu.addAction(self.directionAction)
        self.filterMenu.addAction(self.clearAction)

        self.reportButton = QPushButton()
        self.reportButton.setIcon(QPixmap(u":/icon/res/icon/统计报告.png"))
        self.reportButton.setFixedSize(20, 20)
        self.reportButton.setIconSize(QSize(20, 20))
        self.reportButton.setToolTip("统计报告")
        self.reportButton.setFlat(True)

        # 添加按钮到状态栏
        self.addPermanentWidget(self.reportButton)
        self.addPermanentWidget(self.filterButton)
        self.addPermanentWidget(self.col1)
        self.addPermanentWidget(self.col2)
        self.addPermanentWidget(self.col3)
        self.addPermanentWidget(self.col4)

        # 连接信号槽
        self.filterMenu.triggered.connect(self.handleActionTriggered)

        # 处理函数

    def handleActionTriggered(self, action):
        if action.text() == "清除筛选":
            self.filterButton.setText("筛选")
            globalVar.picPreviewArea.clearFilter()
        elif action.text() == "自定义":
            number, ok = QInputDialog.getDouble(None, "自定义损失比率",
                                                "请输入自定义损失率（0.001-0.999）\n 损失率：(页面面积-图片最大尺寸下面积)/页面面积",
                                                minValue=0.001,
                                                maxValue=0.999,
                                                decimals=3,
                                                step=0.01)
            if ok:
                self.loss_rate = number
                self.filterButton.setText(f"损失率大于{number * 100}%")
                self.loss_rate = number
                globalVar.picPreviewArea.filterByLossRate(number)
            else:
                self.clearAction.setChecked(True)
                self.filterButton.setText("筛选")
                globalVar.picPreviewArea.clearFilter()
        elif action.text() == "图片方向不符":
            globalVar.picPreviewArea.filterByDirection()
            self.filterButton.setText("图片方向不符")
        elif action.text() == "20%":
            globalVar.picPreviewArea.filterByLossRate(0.2)
            self.loss_rate = 0.2
            self.filterButton.setText("损失率大于20%")
        elif action.text() == "30%":
            globalVar.picPreviewArea.filterByLossRate(0.3)
            self.loss_rate = 0.3
            self.filterButton.setText("损失率大于30%")
        elif action.text() == "40%":
            globalVar.picPreviewArea.filterByLossRate(0.4)
            self.loss_rate = 0.4
            self.filterButton.setText("损失率大于40%")
        elif action.text() == "50%":
            globalVar.picPreviewArea.filterByLossRate(0.5)
            self.loss_rate = 0.5
            self.filterButton.setText("损失率大于50%")
        elif action.text() == "60%":
            globalVar.picPreviewArea.filterByLossRate(0.6)
            self.loss_rate = 0.6
            self.filterButton.setText("损失率大于60%")
        print(f"{action.text()} triggered, checked: {action.isChecked()}")

    def colButtonClicked(self, col_num):
        """
        列数按钮点击事件, 设置列数
        :param col_num:
        :return:
        """
        globalVar.picPreviewArea.setColNum(col_num)


class MainWindow(QMainWindow, Ui_MainWindow):
    savePath = None

    def __init__(self):
        super().__init__()

        self.setupUi()
        self.statusBar = StatusBar()
        self.setGlobalVar()

        self.resize(1000, 550)
        self.setUi()

    def setUi(self):
        # 设置状态栏
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("欢迎使用安建排图* ？ *", 5000)

        # Splitter布局比例
        self.splitter.setSizes([1, 1000])
        # 设置拉伸因子
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)

        # 多选按钮，左转右转设置
        self.leftButton.hide()
        self.rightButton.hide()
        self.allButton.hide()
        self.batchButton.clicked.connect(self.multipleButtonClicked)
        self.allButton.clicked.connect(lambda: self.picPreviewArea.selectAll())
        self.leftButton.clicked.connect(lambda: self.picPreviewArea.selectLeft())
        self.rightButton.clicked.connect(lambda: self.picPreviewArea.selectRight())

        # 添加点击按钮
        self.addButton.clicked.connect(self.addImage)

        self.horizontalPage.addItem(template.get_horizontal())
        self.verticalPage.addItem(template.get_vertical())

        self.chooseSavePathButton.clicked.connect(self.chooseSavePath)
        self.startButton.clicked.connect(self.start)

    def addImage(self):
        filename, _ = QFileDialog.getOpenFileNames(None, "添加图片（Ctrl+A-全选）", "", "Images (*.png *.jpg *.jpeg)")
        if filename:
            if self.picPreviewArea.status == PicPreviewAreaStatus.Nothing:
                self.savePath = os.path.join(os.path.split(filename[0])[0], "output.docx")
            self.picPreviewArea.addFiles(filename)

        self.statusBar.showMessage("加载选中图片")

    def setGlobalVar(self):
        globalVar.picPreviewArea = self.picPreviewArea
        globalVar.statusBar = self.statusBar

    def multipleButtonClicked(self):
        if self.picPreviewArea.status == PicPreviewAreaStatus.Normal:
            if self.picPreviewArea.multipleSelect:
                self.picPreviewArea.multipleSelect = False
                self.batchButton.setIcon(QPixmap(u":/icon/res/icon/多选按钮.png"))
                self.leftButton.hide()
                self.allButton.hide()
                self.rightButton.hide()
            else:
                self.picPreviewArea.multipleSelect = True
                self.batchButton.setIcon(QPixmap(u":/icon/res/icon/取消多选.png"))
                self.leftButton.show()
                self.allButton.show()
                self.rightButton.show()

    def chooseSavePath(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "选择保存路径", dir="output.docx")
        if file_path:
            if file_path.endswith(".docx"):
                self.savePath = file_path
                file_path = file_path[:-5]
            else:
                self.savePath = file_path + ".docx"
            self.savePathEdit.setText(file_path)

    def start(self):
        self.statusBar.showMessage("开始生成文档")
        if self.picPreviewArea.status != PicPreviewAreaStatus.Nothing:
            if self.savePath is None:
                print("未选择保存路径")
            save_path = self.savePath
            rows = template.rows()
            cols = template.cols()
            size = template.size()
            margin = template.margin()
            if self.checkBox.isChecked():
                zoom = ImageZoom.CONTAIN
            else:
                zoom = ImageZoom.FILL
            doc = DocumentCreator(rows, cols, size, margin, zoom)
            doc.create(imgTempMemory)
            try:
                doc.document.save(save_path)
            except PermissionError:
                self.statusBar.showMessage("生成失败，文件被占用, 请关闭文件后重试或者选择其他路径")
                new_save_path, _ = QFileDialog.getSaveFileName(None, "选择保存路径", dir="output.docx")
                if new_save_path:
                    if new_save_path.endswith(".docx"):
                        self.savePath = new_save_path
                        new_save_path = new_save_path[:-5]
                    else:
                        self.savePath = new_save_path + ".docx"
                    self.savePathEdit.setText(new_save_path)
                    doc.document.save(new_save_path)
                    self.start()
            self.statusBar.showMessage("文档生成完成")


if __name__ == '__main__':
    extra = {
        # Density Scale
        'density_scale': '-2',
    }

    app = QApplication([])
    THEME_COLORS = apply_stylesheet(app, 'light_blue.xml', invert_secondary=False, extra=extra)
    window = MainWindow()
    window.show()
    app.exec()
