from PySide6.QtCore import QSize, QRect
from PySide6.QtWidgets import QScrollArea, QGridLayout, QWidget
from module.templateItem import TemplateItem
from template import template

class TemplateArea(QScrollArea):
    def __init__(self, parent=None):
        super(TemplateArea, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName(u"scrollArea")
        self.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 476, 243))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.setWidget(self.scrollAreaWidgetContents)

    def addItem(self, templateList: list):
        if len(templateList) % 3 == 0:
            row = len(templateList) // 3
        else:
            row = len(templateList) // 3 + 1
        for row in range(row):
            for col in range(3):
                if row*3 + col >= len(templateList):
                    break
                item = TemplateItem()
                template.registerItem(item)
                item.setInfo(templateList[row*3 + col]["icon"], templateList[row*3 + col]["name"], templateList[row*3 + col]["index"])
                # print(row, col)
                self.gridLayout.addWidget(item, row, col)
