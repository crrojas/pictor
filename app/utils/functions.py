# -*- coding: utf-8 -*-
from PIL import Image
from PySide import QtGui


def pil_to_qimage(pil_img):
    """
    Recieves a PIL image an converts to QImage object
    Source:
    http://qt-project.org/forums/viewthread/5866/#48108
    """
    #im = Image.open("my_image.png")
    data = pil_img.convert("RGBA").tostring('raw', 'RGBA')
    qimage = QtGui.QImage(
        data,
        pil_img.size[0],
        pil_img.size[1],
        QtGui.QImage.Format_ARGB32)
    return qimage
