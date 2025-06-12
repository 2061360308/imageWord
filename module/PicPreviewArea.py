from enum import Enum

from PySide6.QtCore import Signal
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QLabel, QScrollArea, QGridLayout, QWidget

from module.PicPreviewWidget import PicPreviewWidget
from imgTempMemory import imgTempMemory, image_to_qpixmap
from globalVar import globalVar
from template import template
import resources_rc


class Status(Enum):
    Normal = 0
    Nothing = 1
    Loading = 2


class PicFilter:
    """
    封装一些图片筛选方法
    """

    def __init__(self):
        self.filterList = []

    @staticmethod
    def cm_to_pixels(cm, dpi=96):
        inch = cm / 2.54  # 将厘米转换为英寸
        return inch * dpi  # 将英寸转换为像素

    @staticmethod
    def calculate_loss_rate(page_width, page_height, image_width, image_height):
        page_width = PicFilter.cm_to_pixels(page_width)
        page_height = PicFilter.cm_to_pixels(page_height)
        print(page_width, page_height, image_width, image_height)
        # 计算页面面积
        page_area = page_width * page_height

        # 计算图片的缩放比例
        scale = min(page_width / image_width, page_height / image_height)

        # 计算缩放后的图片面积
        image_area = (image_width * scale) * (image_height * scale)

        # 计算空白区域的面积
        blank_area = page_area - image_area

        return blank_area / page_area

    def clearFilter(self):
        """
        清除筛选条件
        :return:
        """
        self.filterList = []

    def filterByDirection(self):
        """
        根据图片方向筛选
        :return:
        """
        # direction: height / width > 1 or < 1
        direction = template.direction()
        self.filterList = []
        for i, ratio in enumerate(imgTempMemory.ratio):
            if direction == 0 and ratio < 1:  # 竖版页面应该删选出横向的图片
                self.filterList.append(i)
            elif direction == 1 and ratio > 1:
                self.filterList.append(i)

    def filterByLossRate(self, loss_rate):
        """
        根据损失率筛选
        :return:
        """
        page_width = template.size()[0] - template.margin()[2] - template.margin()[3]
        page_height = template.size()[1] - template.margin()[0] - template.margin()[1]
        self.filterList = []
        for i, image in enumerate(imgTempMemory.images):
            image_width, image_height = image.size
            rate = self.calculate_loss_rate(page_width, page_height, image_width, image_height)
            print(rate)
            if rate > loss_rate:
                self.filterList.append(i)


class PicPreviewArea(QScrollArea):
    imgLoadedSignal = Signal()
    imgRotateSignal = Signal(int, bool)  # 旋转图片信号 index序号, True为顺时针旋转, False为逆时针旋转
    imgDeleteSignal = Signal(int)  # 删除图片信号
    showImageSignal = Signal(int)  # 显示图片信号

    colNum = 3

    status = Status.Nothing
    multiple_select = False

    def __init__(self, parent=None):
        super(PicPreviewArea, self).__init__(parent)
        self.imgLoadedSignal.connect(self.addImageCallback)
        self.imgRotateSignal.connect(self.rotateImageCallback)
        self.imgDeleteSignal.connect(self.deleteImageCallback)
        self.showImageSignal.connect(self.showImageCallback)

        self.picFilter = PicFilter()
        self.setupUi()
        # self.addFolder("D:/LUAO/Desktop/cstp/")
        self.picPreviewWidgetList = []

    def setupUi(self):
        self.setObjectName(u"scrollArea")
        self.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(0, 0, 476, 1000)
        # self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 3, 0)
        self.setWidget(self.scrollAreaWidgetContents)

        self.placeholderLabel = QLabel(self)
        self.loding_pic = QMovie(u":/icon/res/icon/加载中.gif")
        self.nothing_pic = QPixmap(u":/icon/res/icon/上传文件.png")
        self.nothing()  # 设置状态为无图片状态

    def addFolder(self, folder):
        imgTempMemory.addFolder(folder, self.imgLoadedSignal)
        self.loading()  # 设置状态为加载中

    def addFiles(self, files):
        imgTempMemory.addFiles(files, self.imgLoadedSignal)
        self.loading()  # 设置状态为加载中

    def setColNum(self, num):
        """
        设置列数 只有当当前图片数量大于num时才有效
        :param num: 1,2,3,4
        :return:
        """
        self.colNum = num
        self.clear()
        self.addItem()

    def creatPicPreviewWidget(self):
        """
        创建图片对应的控件
        :return:
        """
        for i in range(len(self.picPreviewWidgetList), len(imgTempMemory.images)):  # 从上一次最后一个开始
            item = PicPreviewWidget(self)
            item.setInfo(imgTempMemory.q_pixmap[i], imgTempMemory.ratio[i], i)
            item.normal()
            self.picPreviewWidgetList.append(item)

    def addImageCallback(self):
        """
        添加新图片回调函数
        :return:
        """
        print("addImageCallback")
        self.creatPicPreviewWidget()  # 为新图片创建控件
        self.addItem()  # 显示图片

    def rotateImageCallback(self, index, clockwise):
        """
        旋转图片回调函数
        :param index: 图片序号
        :param clockwise: 顺时针旋转
        :return:
        """
        print("rotateImageCallback")
        img = imgTempMemory.images[index]
        img = img.rotate(-90 if clockwise else 90, expand=True)
        imgTempMemory.images[index] = img
        q_pixmap = image_to_qpixmap(img)
        imgTempMemory.q_pixmap[index] = q_pixmap
        ratio = img.size[1] / img.size[0]
        imgTempMemory.ratio[index] = ratio
        self.picPreviewWidgetList[index].updateImg(q_pixmap, ratio)
        # self.gridLayout.update()

    def showImageCallback(self, index):
        """
        显示图片回调函数
        :param index: 图片序号
        :return:
        """
        print("showImageCallback")
        img = imgTempMemory.images[index]
        img.show()

    def deleteImageCallback(self, index):
        """
        删除图片回调函数
        :param index: 图片序号
        :return:
        """
        print("deleteImageCallback")
        item = self.picPreviewWidgetList[index]
        imgTempMemory.images.pop(index)
        imgTempMemory.q_pixmap.pop(index)
        imgTempMemory.ratio.pop(index)
        self.picPreviewWidgetList.pop(index)
        item.deleteLater()

        # 更新剩余的编号
        for i in range(index, len(self.picPreviewWidgetList)):
            self.picPreviewWidgetList[i].updateIndex(self.picPreviewWidgetList[i].index - 1)

        # 重新显示图片
        self.clear()
        self.addItem()

    def filterPicPreviewWidgetList(self):
        """
        筛选图片
        :return:
        """

        showWidgetList = []

        # 无筛选条件
        if len(self.picFilter.filterList) == 0:
            return self.picPreviewWidgetList

        # 筛选
        for item in self.picPreviewWidgetList:
            if item.index in self.picFilter.filterList:
                showWidgetList.append(item)

        return showWidgetList

    def addItem(self):
        """
        添加并显示图片
        :return:
        """
        self.normal()  # 设置状态为正常显示状态
        globalVar.statusBar.showMessage("图片加载完成", 5000)

        showWidgetList = self.filterPicPreviewWidgetList()  # 筛选图片
        itemNum = len(showWidgetList)

        if itemNum % 3 == 0:
            row = itemNum // 3
        else:
            row = itemNum // 3 + 1
        for row in range(row):
            for col in range(self.colNum):
                if row * self.colNum + col >= itemNum:
                    break
                showWidgetList[row * self.colNum + col].show()
                self.gridLayout.addWidget(showWidgetList[row * self.colNum + col], row, col)

    def clear(self):
        """
        清空显示所有图片
        :return:
        """
        for item in self.picPreviewWidgetList:
            if self.gridLayout.indexOf(item) != -1:
                self.gridLayout.removeWidget(item)
                item.hide()
        self.gridLayout.update()

    def nothing(self):
        """
        设置状态为无图片状态
        :return:
        """
        self.changeStatus(Status.Nothing)

    def normal(self):
        """
        设置状态为正常显示状态
        :return:
        """
        print("normal")
        self.changeStatus(Status.Normal)

    def loading(self):
        """
        设置状态为加载中
        :return:
        """
        print("loading")
        self.clear()
        self.changeStatus(Status.Loading)

    def changeStatus(self, status: Status):
        self.status = status
        if status == Status.Normal:
            self.gridLayout.removeWidget(self.placeholderLabel)
            self.placeholderLabel.lower()
            self.placeholderLabel.hide()
        else:
            self.gridLayout.addWidget(self.placeholderLabel)
            self.placeholderLabel.show()
            self.placeholderLabel.raise_()
            if status == Status.Loading:
                self.placeholderLabel.setMovie(self.loding_pic)
                self.placeholderLabel.setFixedSize(240, 240)
                self.loding_pic.start()
            elif status == Status.Nothing:
                self.placeholderLabel.setPixmap(self.nothing_pic)
                self.placeholderLabel.setFixedSize(150, 130)
                self.placeholderLabel.setScaledContents(True)

    def changeColNum(self, num):
        self.colNum = num
        self.clear()
        self.addItem()

    @property
    def multipleSelect(self):
        return self.multiple_select

    @multipleSelect.setter
    def multipleSelect(self, value):
        if value == self.multiple_select:
            return
        self.multiple_select = value
        showWidgetList = self.filterPicPreviewWidgetList()  # 筛选图片
        for item in showWidgetList:
            if value:
                item.select()
            else:
                item.normal()

    def selectAll(self):
        """
        全选
        翻转所有图片的选中状态
        :return:
        """
        if self.multiple_select:  # 多选状态下才有效
            showWidgetList = self.filterPicPreviewWidgetList()
            for item in showWidgetList:
                if item.checkBox.isChecked():
                    item.checkBox.setChecked(False)
                else:
                    item.checkBox.setChecked(True)

    def selectLeft(self):
        """
        选中的左转
        :return:
        """
        if self.multiple_select:  # 多选状态下才有效
            showWidgetList = self.filterPicPreviewWidgetList()
            for item in showWidgetList:
                if item.checkBox.isChecked():
                    self.imgRotateSignal.emit(item.index, False)

    def selectRight(self):
        """
        选中的右转
        :return:
        """
        if self.multiple_select:
            showWidgetList = self.filterPicPreviewWidgetList()
            for item in showWidgetList:
                if item.checkBox.isChecked():
                    self.imgRotateSignal.emit(item.index, True)

    def filterByDirection(self):
        if self.status == Status.Normal:
            self.clear()
            self.loading()
            self.picFilter.filterByDirection()
            self.addItem()
            self.normal()
            globalVar.statusBar.showMessage("筛选完成", 5000)

    def clearFilter(self):
        if self.status == Status.Normal:
            self.clear()
            self.picFilter.clearFilter()
            self.addItem()
            self.normal()
            globalVar.statusBar.showMessage("清除筛选条件", 5000)

    def filterByLossRate(self, loss_rate):
        if self.status == Status.Normal:
            self.clear()
            self.loading()
            self.picFilter.filterByLossRate(loss_rate)
            self.addItem()
            self.normal()
            globalVar.statusBar.showMessage("筛选完成", 5000)
