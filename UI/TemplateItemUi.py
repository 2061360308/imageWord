# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TemplateItemUi.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_TemplateItem(object):
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"TemplateItem")
        self.resize(349, 288)
        self.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.iconLabel = QLabel(self)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setMinimumSize(QSize(85, 85))
        self.iconLabel.setMaximumSize(QSize(85, 85))
        self.iconLabel.setPixmap(QPixmap(u":/template/res/template/一行一列.png"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.iconLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.nameLabel = QLabel(self)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setMinimumSize(QSize(0, 20))
        self.nameLabel.setMaximumSize(QSize(16777215, 20))
        self.nameLabel.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.nameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.nameLabel)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("TemplateItem", u"Form", None))
        self.iconLabel.setText("")
        self.nameLabel.setText(QCoreApplication.translate("TemplateItem", u"一行一列", None))
    # retranslateUi

