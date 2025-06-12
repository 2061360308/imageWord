# -*- coding: utf-8 -*-
from enum import Enum
import time
from PIL import Image
################################################################################
## Form generated from reading UI file 'self.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QSize, Qt, QTimer)
from PySide6.QtGui import (QIcon, QPixmap)
from PySide6.QtWidgets import (QCheckBox, QHBoxLayout, QLabel,
                               QPushButton, QWidget)


class Status(Enum):
    Normal = 0
    Hover = 1
    Select = 2


class PicPreviewWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        self.index = None
        self.ratio = 1

        self.status = Status.Normal
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"PicPreviewWidget")
        self.controlWidget = QWidget(self)
        self.controlWidget.move(0, 0)
        self.controlWidget.setStyleSheet("background-color: rgba(255, 255, 255, 50);")  # 设置背景颜色为白色，# 设置透明度
        self.horizontalLayout_2 = QHBoxLayout(self.controlWidget)
        self.leftButton = QPushButton(self.controlWidget)
        self.leftButton.clicked.connect(lambda: self.parent.imgRotateSignal.emit(self.index, False))
        self.leftButton.setIcon(QIcon(u":/icon/res/icon/翻转90度.png"))
        self.leftButton.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 150);
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 255);
            }
        """)
        self.leftButton.setIconSize(QSize(32, 32))
        self.leftButton.setFixedSize(40, 40)  # 设置按钮的宽度和高度
        self.leftButton.setFlat(True)
        self.horizontalLayout_2.addWidget(self.leftButton)
        self.openButton = QPushButton(self.controlWidget)
        self.openButton.clicked.connect(lambda: self.parent.showImageSignal.emit(self.index))
        self.openButton.setIcon(QIcon(u":/icon/res/icon/查看.png"))
        self.openButton.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255, 255, 255, 150);
                        border-radius: 20px;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 255, 255, 255);
                    }
                """)
        self.openButton.setIconSize(QSize(32, 32))
        self.openButton.setFixedSize(40, 40)
        self.openButton.setFlat(True)
        self.horizontalLayout_2.addWidget(self.openButton)
        self.rightButton = QPushButton(self.controlWidget)
        self.rightButton.clicked.connect(lambda: self.parent.imgRotateSignal.emit(self.index, True))
        self.rightButton.setIcon(QIcon(u":/icon/res/icon/翻转90度2.png"))
        self.rightButton.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255, 255, 255, 150);
                        border-radius: 20px;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 255, 255, 255);
                    }
                """)
        self.rightButton.setIconSize(QSize(32, 32))
        self.rightButton.setFixedSize(40, 40)
        self.rightButton.setFlat(True)
        self.horizontalLayout_2.addWidget(self.rightButton)

        # 复选框
        self.checkBox = QCheckBox(self)
        self.checkBox.move(0, 0)

        # 预览图片
        self.preLabel = QLabel(self)
        self.preLabel.move(0, 0)
        self.preLabel.setScaledContents(True)

        # 删除按钮
        self.delButton = QPushButton(self)
        self.delButton.clicked.connect(lambda: self.parent.imgDeleteSignal.emit(self.index))
        self.delButton.setIcon(QIcon(u":/icon/res/icon/删除.png"))
        self.delButton.setFlat(True)
        self.delButton.setStyleSheet("""background-color: rgba(255, 0, 0, 255);""")
        self.delButton.setIconSize(QSize(20, 20))
        self.delButton.setFixedSize(QSize(20, 20))

        # 编号标签
        self.indexLabel = QLabel(self)
        self.indexLabel.setFixedHeight(20)
        self.indexLabel.setMinimumWidth(20)
        self.indexLabel.setStyleSheet("""background-color: rgba(255, 255, 255, 255);font: 700 11pt;""")
        self.indexLabel.setAlignment(Qt.AlignCenter)

        # 创建一个定时器
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.handleResize)

    def setInfo(self, q_pixmax: QPixmap, ratio: float, index: int):
        self.ratio = ratio
        self.preLabel.setPixmap(q_pixmax)
        self.index = index

        self.indexLabel.setText(str(self.index + 1))

    def resizeEvent(self, event):
        self.timer.start(500)

    def handleResize(self):
        # 在定时器超时时处理窗口大小改变
        try:
            self.setMinimumHeight(int(self.width() * self.ratio))
            self.preLabel.resize(self.width(), int(self.width() * self.ratio))
            if self.width() * self.ratio < self.height():
                self.preLabel.move(0, (self.height() - self.width() * self.ratio) // 2)
            else:
                self.preLabel.move(0, 0)
            self.indexLabel.move(self.width() - self.indexLabel.width(), self.height() - 20)
        except Exception as e:
            print(e)

    def select(self):
        self.status = Status.Select
        self.changeDisplay()
        self.checkBox.raise_()

    def hover(self):
        self.status = Status.Hover

        # 调整按钮大小位置
        self.controlWidget.resize(self.width(), int(self.width() * self.ratio))
        if self.width() * self.ratio < self.height():
            self.controlWidget.move(0, (self.height() - self.width() * self.ratio) // 2)
        self.delButton.move(self.width() - 20, 0)

        # 调整按钮显示顺序
        self.controlWidget.raise_()
        self.delButton.raise_()
        self.indexLabel.raise_()

        # 调整按钮显示状态
        self.changeDisplay()

    def normal(self):
        self.status = Status.Normal
        self.changeDisplay()
        self.checkBox.setChecked(False)  # 退出多选的时候取消选中，恢复状态

    def changeDisplay(self):
        if self.status == Status.Normal:
            self.controlWidget.hide()
            self.checkBox.hide()
            self.delButton.hide()
        elif self.status == Status.Hover:
            self.controlWidget.show()
            self.checkBox.hide()
            self.delButton.show()
        elif self.status == Status.Select:
            self.controlWidget.hide()
            self.checkBox.show()
            self.delButton.hide()
        self.update()

    def enterEvent(self, event):
        if self.status != Status.Select:
            self.hover()

    def leaveEvent(self, event):
        if self.status != Status.Select:
            self.normal()

    def updateImg(self, img: QPixmap, ratio: float):
        self.preLabel.setPixmap(img)
        self.ratio = ratio
        self.handleResize()

    def updateIndex(self, index: int):
        self.index = index
        self.indexLabel.setText(str(self.index + 1))

    def mousePressEvent(self, event):
        # 多选状态下点击图片，选中或取消选中
        if self.status == Status.Select:
            self.checkBox.setChecked(not self.checkBox.isChecked())
