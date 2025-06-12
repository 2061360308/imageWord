# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowUi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QStatusBar, QTabWidget, QToolBox, QVBoxLayout,
    QWidget)

from module.PicPreviewArea import PicPreviewArea
from module.TemplateArea import TemplateArea
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(691, 475)
        icon = QIcon()
        icon.addFile(u":/icon/res/icon/打印.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.savePathEdit = QLineEdit(self.centralwidget)
        self.savePathEdit.setObjectName(u"savePathEdit")
        self.savePathEdit.setFrame(False)
        self.savePathEdit.setDragEnabled(False)
        self.savePathEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.savePathEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.chooseSavePathButton = QPushButton(self.centralwidget)
        self.chooseSavePathButton.setObjectName(u"chooseSavePathButton")
        self.chooseSavePathButton.setMinimumSize(QSize(28, 28))
        self.chooseSavePathButton.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icon/res/icon/选择文件.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chooseSavePathButton.setIcon(icon1)
        self.chooseSavePathButton.setIconSize(QSize(28, 28))
        self.chooseSavePathButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.chooseSavePathButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(32, 32))
        self.startButton.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/icon/res/icon/开始.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startButton.setIcon(icon2)
        self.startButton.setIconSize(QSize(32, 32))
        self.startButton.setAutoExclusive(False)
        self.startButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.startButton)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        icon3 = QIcon()
        icon3.addFile(u":/icon/res/icon/添加.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addButton.setIcon(icon3)
        self.addButton.setIconSize(QSize(32, 32))
        self.addButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.addButton)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.batchButton = QPushButton(self.centralwidget)
        self.batchButton.setObjectName(u"batchButton")
        self.batchButton.setMinimumSize(QSize(32, 32))
        self.batchButton.setMaximumSize(QSize(32, 32))
        self.batchButton.setStyleSheet(u"font: 700 10pt \"Microsoft YaHei UI\";")
        icon4 = QIcon()
        icon4.addFile(u":/icon/res/icon/多选按钮.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.batchButton.setIcon(icon4)
        self.batchButton.setIconSize(QSize(20, 20))
        self.batchButton.setFlat(True)

        self.horizontalLayout_15.addWidget(self.batchButton)

        self.allButton = QPushButton(self.centralwidget)
        self.allButton.setObjectName(u"allButton")
        self.allButton.setMinimumSize(QSize(32, 32))
        self.allButton.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/icon/res/icon/全选-选择.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.allButton.setIcon(icon5)
        self.allButton.setIconSize(QSize(20, 20))
        self.allButton.setFlat(True)

        self.horizontalLayout_15.addWidget(self.allButton)

        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setMinimumSize(QSize(32, 32))
        self.leftButton.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/icon/res/icon/翻转90度.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leftButton.setIcon(icon6)
        self.leftButton.setIconSize(QSize(25, 25))
        self.leftButton.setFlat(True)

        self.horizontalLayout_15.addWidget(self.leftButton)

        self.rightButton = QPushButton(self.centralwidget)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setMinimumSize(QSize(32, 32))
        self.rightButton.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/icon/res/icon/翻转90度2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rightButton.setIcon(icon7)
        self.rightButton.setIconSize(QSize(25, 25))
        self.rightButton.setFlat(True)

        self.horizontalLayout_15.addWidget(self.rightButton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.simplePage = QWidget()
        self.simplePage.setObjectName(u"simplePage")
        self.horizontalLayout_3 = QHBoxLayout(self.simplePage)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.simpleWidget = QToolBox(self.simplePage)
        self.simpleWidget.setObjectName(u"simpleWidget")
        self.simpleWidget.setFrameShape(QFrame.NoFrame)
        self.verticalPage = TemplateArea()
        self.verticalPage.setObjectName(u"verticalPage")
        self.verticalPage.setGeometry(QRect(0, 0, 553, 245))
        self.horizontalLayout = QHBoxLayout(self.verticalPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        icon8 = QIcon()
        icon8.addFile(u":/icon/res/icon/两行.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.simpleWidget.addItem(self.verticalPage, icon8, u"竖版文档")
        self.horizontalPage = TemplateArea()
        self.horizontalPage.setObjectName(u"horizontalPage")
        self.horizontalPage.setGeometry(QRect(0, 0, 553, 245))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalPage)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        icon9 = QIcon()
        icon9.addFile(u":/icon/res/icon/两列.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.simpleWidget.addItem(self.horizontalPage, icon9, u"横版文档")

        self.verticalLayout.addWidget(self.simpleWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.simplePage)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        icon10 = QIcon()
        icon10.addFile(u":/icon/res/icon/模板.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.simplePage, icon10, "")
        self.seniorPage = QWidget()
        self.seniorPage.setObjectName(u"seniorPage")
        self.verticalLayout_4 = QVBoxLayout(self.seniorPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.seniorPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(32, 32))
        self.label_5.setMaximumSize(QSize(32, 32))
        self.label_5.setPixmap(QPixmap(u":/icon/res/icon/纸张大小.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_3 = QLabel(self.seniorPage)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.LabelRole, self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pageWidthBox = QDoubleSpinBox(self.seniorPage)
        self.pageWidthBox.setObjectName(u"pageWidthBox")

        self.horizontalLayout_6.addWidget(self.pageWidthBox)

        self.label_4 = QLabel(self.seniorPage)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.pageHeightBox = QDoubleSpinBox(self.seniorPage)
        self.pageHeightBox.setObjectName(u"pageHeightBox")

        self.horizontalLayout_6.addWidget(self.pageHeightBox)

        self.pageUnitBox = QComboBox(self.seniorPage)
        self.pageUnitBox.addItem("")
        self.pageUnitBox.addItem("")
        self.pageUnitBox.addItem("")
        self.pageUnitBox.setObjectName(u"pageUnitBox")

        self.horizontalLayout_6.addWidget(self.pageUnitBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pageModelBox = QComboBox(self.seniorPage)
        self.pageModelBox.addItem("")
        self.pageModelBox.addItem("")
        self.pageModelBox.addItem("")
        self.pageModelBox.addItem("")
        self.pageModelBox.setObjectName(u"pageModelBox")
        self.pageModelBox.setMinimumSize(QSize(80, 0))
        self.pageModelBox.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_6.addWidget(self.pageModelBox)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.seniorPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(32, 32))
        self.label_7.setMaximumSize(QSize(32, 32))
        self.label_7.setPixmap(QPixmap(u":/icon/res/icon/页边距.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_6 = QLabel(self.seniorPage)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)

        self.comboBox_7 = QComboBox(self.seniorPage)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_10.addWidget(self.comboBox_7)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.LabelRole, self.horizontalLayout_10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.seniorPage)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.upMarginBox = QDoubleSpinBox(self.seniorPage)
        self.upMarginBox.setObjectName(u"upMarginBox")

        self.horizontalLayout_8.addWidget(self.upMarginBox)

        self.upMarginUnitBox = QComboBox(self.seniorPage)
        self.upMarginUnitBox.addItem("")
        self.upMarginUnitBox.addItem("")
        self.upMarginUnitBox.addItem("")
        self.upMarginUnitBox.setObjectName(u"upMarginUnitBox")

        self.horizontalLayout_8.addWidget(self.upMarginUnitBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.label_9 = QLabel(self.seniorPage)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.downMarginBox = QDoubleSpinBox(self.seniorPage)
        self.downMarginBox.setObjectName(u"downMarginBox")

        self.horizontalLayout_8.addWidget(self.downMarginBox)

        self.downMarginUnitBox = QComboBox(self.seniorPage)
        self.downMarginUnitBox.addItem("")
        self.downMarginUnitBox.addItem("")
        self.downMarginUnitBox.addItem("")
        self.downMarginUnitBox.setObjectName(u"downMarginUnitBox")

        self.horizontalLayout_8.addWidget(self.downMarginUnitBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.seniorPage)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.leftMarginBox = QDoubleSpinBox(self.seniorPage)
        self.leftMarginBox.setObjectName(u"leftMarginBox")

        self.horizontalLayout_9.addWidget(self.leftMarginBox)

        self.leftMarginUnitBox = QComboBox(self.seniorPage)
        self.leftMarginUnitBox.addItem("")
        self.leftMarginUnitBox.addItem("")
        self.leftMarginUnitBox.addItem("")
        self.leftMarginUnitBox.setObjectName(u"leftMarginUnitBox")

        self.horizontalLayout_9.addWidget(self.leftMarginUnitBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.label_11 = QLabel(self.seniorPage)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.rightMarginBox = QDoubleSpinBox(self.seniorPage)
        self.rightMarginBox.setObjectName(u"rightMarginBox")

        self.horizontalLayout_9.addWidget(self.rightMarginBox)

        self.rightMaginUnitBox = QComboBox(self.seniorPage)
        self.rightMaginUnitBox.addItem("")
        self.rightMaginUnitBox.addItem("")
        self.rightMaginUnitBox.addItem("")
        self.rightMaginUnitBox.setObjectName(u"rightMaginUnitBox")

        self.horizontalLayout_9.addWidget(self.rightMaginUnitBox)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.verticalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.seniorPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(28, 28))
        self.label_13.setMaximumSize(QSize(28, 28))
        self.label_13.setPixmap(QPixmap(u":/icon/res/icon/斜角缩放.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.label_12 = QLabel(self.seniorPage)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.LabelRole, self.horizontalLayout_11)

        self.scaleBox = QComboBox(self.seniorPage)
        self.scaleBox.addItem("")
        self.scaleBox.addItem("")
        self.scaleBox.addItem("")
        self.scaleBox.setObjectName(u"scaleBox")
        self.scaleBox.setMaximumSize(QSize(180, 16777215))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.scaleBox)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.seniorPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(32, 32))
        self.label_15.setMaximumSize(QSize(32, 32))
        self.label_15.setPixmap(QPixmap(u":/icon/res/icon/层次排布.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_15)

        self.label_14 = QLabel(self.seniorPage)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)


        self.formLayout.setLayout(3, QFormLayout.ItemRole.LabelRole, self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.rowNumBox = QSpinBox(self.seniorPage)
        self.rowNumBox.setObjectName(u"rowNumBox")
        self.rowNumBox.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_13.addWidget(self.rowNumBox)

        self.label_16 = QLabel(self.seniorPage)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.colNumBox = QSpinBox(self.seniorPage)
        self.colNumBox.setObjectName(u"colNumBox")
        self.colNumBox.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_13.addWidget(self.colNumBox)

        self.label_17 = QLabel(self.seniorPage)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_13)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.seniorPage)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.addTemplateButton = QPushButton(self.groupBox)
        self.addTemplateButton.setObjectName(u"addTemplateButton")
        icon11 = QIcon()
        icon11.addFile(u":/icon/res/icon/添加到模板.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addTemplateButton.setIcon(icon11)
        self.addTemplateButton.setIconSize(QSize(20, 20))
        self.addTemplateButton.setFlat(True)

        self.horizontalLayout_14.addWidget(self.addTemplateButton)

        self.addMenuButton = QPushButton(self.groupBox)
        self.addMenuButton.setObjectName(u"addMenuButton")
        icon12 = QIcon()
        icon12.addFile(u":/icon/res/icon/添加右击菜单.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addMenuButton.setIcon(icon12)
        self.addMenuButton.setIconSize(QSize(20, 20))
        self.addMenuButton.setFlat(True)

        self.horizontalLayout_14.addWidget(self.addMenuButton)

        self.settingButton = QPushButton(self.groupBox)
        self.settingButton.setObjectName(u"settingButton")
        icon13 = QIcon()
        icon13.addFile(u":/icon/res/icon/管理.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingButton.setIcon(icon13)
        self.settingButton.setIconSize(QSize(20, 20))
        self.settingButton.setFlat(True)

        self.horizontalLayout_14.addWidget(self.settingButton)


        self.verticalLayout_4.addWidget(self.groupBox)

        icon14 = QIcon()
        icon14.addFile(u":/icon/res/icon/高级模式.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.seniorPage, icon14, "")
        self.splitter.addWidget(self.tabWidget)
        self.picPreviewArea = PicPreviewArea(self.splitter)
        self.picPreviewArea.setObjectName(u"picPreviewArea")
        self.splitter.addWidget(self.picPreviewArea)

        self.verticalLayout_5.addWidget(self.splitter)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        self.tabWidget.setCurrentIndex(0)
        self.simpleWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"安建排图", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"保存位置", None))
        self.savePathEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%第一张图片同级目录%/output", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u".docx", None))
        self.chooseSavePathButton.setText("")
#if QT_CONFIG(tooltip)
        self.startButton.setToolTip(QCoreApplication.translate("MainWindow", u"开始排图", None))
#endif // QT_CONFIG(tooltip)
        self.startButton.setText("")
#if QT_CONFIG(tooltip)
        self.addButton.setToolTip(QCoreApplication.translate("MainWindow", u"添加文件", None))
#endif // QT_CONFIG(tooltip)
        self.addButton.setText("")
#if QT_CONFIG(tooltip)
        self.batchButton.setToolTip(QCoreApplication.translate("MainWindow", u"多选", None))
#endif // QT_CONFIG(tooltip)
        self.batchButton.setText("")
#if QT_CONFIG(tooltip)
        self.allButton.setToolTip(QCoreApplication.translate("MainWindow", u"全部选择", None))
#endif // QT_CONFIG(tooltip)
        self.allButton.setText("")
        self.leftButton.setText("")
        self.rightButton.setText("")
        self.simpleWidget.setItemText(self.simpleWidget.indexOf(self.verticalPage), QCoreApplication.translate("MainWindow", u"竖版文档", None))
        self.simpleWidget.setItemText(self.simpleWidget.indexOf(self.horizontalPage), QCoreApplication.translate("MainWindow", u"横版文档", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"锁定长宽比", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.simplePage), QCoreApplication.translate("MainWindow", u"简易模版", None))
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"纸张大小", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"×", None))
        self.pageUnitBox.setItemText(0, QCoreApplication.translate("MainWindow", u"厘米（Cm）", None))
        self.pageUnitBox.setItemText(1, QCoreApplication.translate("MainWindow", u"像素（px）", None))
        self.pageUnitBox.setItemText(2, QCoreApplication.translate("MainWindow", u"英尺（Ft）", None))

        self.pageModelBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A4", None))
        self.pageModelBox.setItemText(1, QCoreApplication.translate("MainWindow", u"A3", None))
        self.pageModelBox.setItemText(2, QCoreApplication.translate("MainWindow", u"B4", None))
        self.pageModelBox.setItemText(3, QCoreApplication.translate("MainWindow", u"B5", None))

        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"页边距", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"普通", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"窄", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"适中", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"宽", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"上", None))
        self.upMarginBox.setPrefix("")
        self.upMarginBox.setSuffix("")
        self.upMarginUnitBox.setItemText(0, QCoreApplication.translate("MainWindow", u"厘米Cm", None))
        self.upMarginUnitBox.setItemText(1, QCoreApplication.translate("MainWindow", u"像素Px", None))
        self.upMarginUnitBox.setItemText(2, QCoreApplication.translate("MainWindow", u"英尺Ft", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"下", None))
        self.downMarginUnitBox.setItemText(0, QCoreApplication.translate("MainWindow", u"厘米Cm", None))
        self.downMarginUnitBox.setItemText(1, QCoreApplication.translate("MainWindow", u"像素Px", None))
        self.downMarginUnitBox.setItemText(2, QCoreApplication.translate("MainWindow", u"英尺Ft", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"左", None))
        self.leftMarginBox.setPrefix("")
        self.leftMarginBox.setSuffix("")
        self.leftMarginUnitBox.setItemText(0, QCoreApplication.translate("MainWindow", u"厘米Cm", None))
        self.leftMarginUnitBox.setItemText(1, QCoreApplication.translate("MainWindow", u"像素Px", None))
        self.leftMarginUnitBox.setItemText(2, QCoreApplication.translate("MainWindow", u"英尺Ft", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"右", None))
        self.rightMaginUnitBox.setItemText(0, QCoreApplication.translate("MainWindow", u"厘米Cm", None))
        self.rightMaginUnitBox.setItemText(1, QCoreApplication.translate("MainWindow", u"像素Px", None))
        self.rightMaginUnitBox.setItemText(2, QCoreApplication.translate("MainWindow", u"英尺Ft", None))

        self.label_13.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"缩放方式", None))
        self.scaleBox.setItemText(0, QCoreApplication.translate("MainWindow", u"拉升（丢失长宽比）", None))
        self.scaleBox.setItemText(1, QCoreApplication.translate("MainWindow", u"填充（留有有空白）", None))
        self.scaleBox.setItemText(2, QCoreApplication.translate("MainWindow", u"裁剪（丢失图像内容）", None))

        self.label_15.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"排布方式", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"行", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"列", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"其他设置", None))
        self.addTemplateButton.setText(QCoreApplication.translate("MainWindow", u"列为模板", None))
        self.addMenuButton.setText(QCoreApplication.translate("MainWindow", u"添加右击菜单", None))
#if QT_CONFIG(tooltip)
        self.settingButton.setToolTip(QCoreApplication.translate("MainWindow", u"管理", None))
#endif // QT_CONFIG(tooltip)
        self.settingButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.seniorPage), QCoreApplication.translate("MainWindow", u"高级模式", None))
    # retranslateUi

