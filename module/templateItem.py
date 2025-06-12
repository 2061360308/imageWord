from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from UI.TemplateItemUi import Ui_TemplateItem
from globalVar import globalVar
from template import template


# import resources_rc


class TemplateItem(QWidget, Ui_TemplateItem):
    index = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi()
        self.iconLabel.setStyleSheet("#currentTemplateLabel { background-color: rgba(98, 144, 250, 100); }")
        # self.setStyleSheet("background-color:red;")

    def setInfo(self, icon, name, index):
        self.index = index
        self.iconLabel.setPixmap(QPixmap(u":/template/res/template/%s.png" % icon))
        self.nameLabel.setText(name)
        self.updateCurrentStyle()

    def updateCurrentStyle(self):
        if self.index == template.current:
            self.iconLabel.setObjectName("currentTemplateLabel")
        else:
            self.iconLabel.setObjectName("templateLabel")

        self.iconLabel.style().unpolish(self.iconLabel)
        self.iconLabel.style().polish(self.iconLabel)
        self.iconLabel.update()

    def mousePressEvent(self, event):
        template.current = self.index

        # 根据新的页面设置应用之前的筛选情况
        current_filter = globalVar.statusBar.actionGroup.checkedAction().text()
        if current_filter == "图片方向不符":
            globalVar.picPreviewArea.filterByDirection()
        elif current_filter == "清除筛选":
            pass
        else:
            globalVar.picPreviewArea.filterByLossRate(globalVar.statusBar.loss_rate)

