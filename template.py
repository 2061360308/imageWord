# 模板管理
from userData import getTemplate


class Template:
    __current = 0  # 当前模板
    template = getTemplate()  # 模板数据

    useTemplate = True  # 使用的模板

    templateItemList = []

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, index):
        """
        设置当前的值, 并通知各个templateItem更新状态
        :param index:
        :return:
        """
        self.__current = index
        for item in self.templateItemList:
            item.updateCurrentStyle()

    def get_horizontal(self) -> list:
        """
        获取横向模板
        :return:
        """
        return [item for item in self.template if item["direction"] == 1]

    def get_vertical(self) -> list:
        """
        获取纵向模板
        :return: [name, icon, arrangement, size, margin, direction, index]
        """
        return [item for item in self.template if item["direction"] == 0]

    def registerItem(self, item):
        self.templateItemList.append(item)

    def size(self):
        if self.useTemplate:
            return self.template[self.current]["size"]

    def margin(self):
        if self.useTemplate:
            return self.template[self.current]["margin"]

    def rows(self):
        if self.useTemplate:
            return self.template[self.current]["arrangement"][0]

    def cols(self):
        if self.useTemplate:
            return self.template[self.current]["arrangement"][1]

    def arrangement(self):
        if self.useTemplate:
            return self.template[self.current]["arrangement"]

    def direction(self):
        if self.useTemplate:
            return self.template[self.current]["direction"]


template = Template()
