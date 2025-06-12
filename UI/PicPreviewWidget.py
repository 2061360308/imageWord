# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_PicPreviewWidget(object):
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"PicPreviewWidget")
        self.resize(458, 425)
        self.controlWidget = QWidget(self)
        self.controlWidget.setObjectName(u"controlWidget")
        self.controlWidget.setGeometry(QRect(30, 160, 371, 261))
        self.controlWidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.controlWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftButton = QPushButton(self.controlWidget)
        self.leftButton.setObjectName(u"leftButton")

        self.horizontalLayout_2.addWidget(self.leftButton)

        self.openButton = QPushButton(self.controlWidget)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout_2.addWidget(self.openButton)

        self.rightButton = QPushButton(self.controlWidget)
        self.rightButton.setObjectName(u"rightButton")

        self.horizontalLayout_2.addWidget(self.rightButton)

        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 261, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.preLabel = QLabel(self)
        self.preLabel.setObjectName(u"preLabel")
        self.preLabel.setGeometry(QRect(50, 60, 341, 71))

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("PicPreviewWidget", u"Form", None))
        self.leftButton.setText("")
        self.openButton.setText("")
        self.rightButton.setText("")
        self.checkBox.setText("")
        self.preLabel.setText("")
    # retranslateUi

