class GlobalVar:
    __picPreviewArea = None
    __statusBar = None

    @property
    def picPreviewArea(self):
        return self.__picPreviewArea

    @picPreviewArea.setter
    def picPreviewArea(self, value):
        self.__picPreviewArea = value

    @property
    def statusBar(self):
        return self.__statusBar

    @statusBar.setter
    def statusBar(self, value):
        self.__statusBar = value


globalVar = GlobalVar()
