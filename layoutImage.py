from os.path import join, exists, basename
from sys import argv, exit
from time import time

from documentCreator import DocumentCreator, ImageZoom
from imgTempMemory import imgTempMemory

if len(argv) == 7:
    folderPath = argv[1]
    rows = int(argv[2])
    cols = int(argv[3])
    size = tuple(argv[4].split(","))
    margin = tuple(argv[5].split(","))
    zoom = ImageZoom(int(argv[6]))
elif len(argv) == 5:
    folderPath = argv[1]
    rows = int(argv[2])
    cols = int(argv[3])
    zoom = ImageZoom(int(argv[4]))

    size = (21, 29.7)
    margin = (0.5, 0.5, 0.5, 0.5)
else:
    print("Usage: layoutImage.exe folderPath rows cols size margin zoom\nlayoutImage.exe folderPath rows cols "
          "zoom\nsize: 21,29.7\nmargin: 0.5,0.5,0.5,0.5\nzoom: 0-4")
    exit(1)

if not exists(folderPath):
    print(f"Folder({folderPath}) not exists")
    exit(2)

folderName = basename(folderPath)  # 获取文件夹名称
outputPath = join(folderPath, "../", f"{folderName}-{time()}.docx")

imgTempMemory.addFolder(folderPath, None, True)
doc = DocumentCreator(rows, cols, size, margin, zoom)
doc.create(imageTempMemory=imgTempMemory)
doc.document.save(outputPath)

