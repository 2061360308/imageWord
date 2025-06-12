from os import walk
from os.path import isfile, isdir, join
from threading import Thread
from PIL import Image

images = []
q_pixmap = []
ratio = []


def image_to_qpixmap(pil_image):
    from PySide6.QtGui import QImage, QPixmap
    # 将PIL Image对象转换为QPixmap
    # print(pil_image.mode)
    if pil_image.mode != 'RGBA':
        pil_image = pil_image.convert('RGBA')
        # 调整颜色通道的顺序
    r, g, b, a = pil_image.split()
    pil_image = Image.merge('RGBA', (b, g, r, a))
    data = pil_image.tobytes('raw', 'RGBA')
    qimage = QImage(data, pil_image.size[0], pil_image.size[1], QImage.Format_ARGB32)
    return QPixmap.fromImage(qimage)


class LoadImgThread(Thread):
    def __init__(self):
        super().__init__()
        self.img_path = []
        self.signal = None

    def task(self, img_path: list, signal=None, qt=False):
        self.img_path = img_path
        self.qt = qt
        self.signal = signal

    def run(self):
        for img in self.img_path:
            if isfile(img):
                if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
                    image = Image.open(img)
                    images.append(image)
                    if self.qt:
                        q_pixmap.append(image_to_qpixmap(image))
                        ratio.append(image.size[1] / image.size[0])
        if self.signal:
            self.signal.emit()


class ImgTempMemory:
    def __init__(self, qt=False):
        global images
        self.images = images
        self.q_pixmap = q_pixmap
        self.ratio = ratio
        self.qt = qt

    def addFolder(self, path, signal=None, wait=False):
        print("addFolder imgae")
        img_path = []
        if isdir(path):
            for root, dirs, files in walk(path):
                for file in files:
                    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                        img_path.append(join(root, file))
        self.addFiles(img_path, signal, wait)

    def addFiles(self, img_path: list, signal=None, wait=False):
        # 给定信号说明需要生成QPixmap
        if signal:
            qt = True
        else:
            qt = False
        loadImgThread = LoadImgThread()
        loadImgThread.task(img_path, signal, qt)
        loadImgThread.start()
        if wait:
            loadImgThread.join()

    def addFile(self, img):
        if isfile(img):
            if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
                self.images.append(Image.open(img))

    def images(self):
        for image in self.images:
            yield image


imgTempMemory = ImgTempMemory()
