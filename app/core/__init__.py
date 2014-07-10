# -*- coding: utf-8 -*-
import os
import sys
from itertools import chain
from collections import namedtuple


VERSION = "0.9.18"
APPNAME = "Pictor"

Format = namedtuple('Format', ['name', 'ext'])

supported_formats = (
    Format(name="PNG", ext=["PNG", "png"]),
    Format(name="JPG", ext=["JPG", "jpg", "JPEG", "jpeg"]),
    Format(name="TIF", ext=["TIF", "tif", "TIFF", "tiff"]))


def formats():
    return " *.".join(reduce(chain, [f.ext for f in supported_formats]))


if sys.platform.startswith('darwin'):
    from AppKit import NSSearchPathForDirectoriesInDomains
    APPDATA = os.path.join(
        NSSearchPathForDirectoriesInDomains(14, 1, True)[0],
        APPNAME).decode(sys.getfilesystemencoding())

elif sys.platform.startswith('win'):
    APPDATA = os.path.join(
        os.environ['APPDATA'], APPNAME).decode(
        sys.getfilesystemencoding())
else:
    APPDATA = os.path.expanduser(
        os.path.join("~", "." + APPNAME)).decode(
        sys.getfilesystemencoding())
#create the main folder data
if not os.path.exists(APPDATA):
    os.makedirs(APPDATA)

TUMB_PATH = os.path.join(APPDATA, "statics", "thumbnail")
if not os.path.exists(TUMB_PATH):
    os.makedirs(TUMB_PATH)
