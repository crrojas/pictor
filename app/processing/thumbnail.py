# -*- coding: utf-8 -*-
import os
from collections import namedtuple
from core import TUMB_PATH
from utils import pil_to_qimage
from PIL import Image


Size = namedtuple('Size', ['width', 'height'])

step_size = Size(width=500, height=500)
max_size = Size(width=150, height=150)


def thumbnail(img_path):
    """
    Given a path returns an image thumbnail object
    This link recomended two steps for thumbnails
    http://united-coders.com/christian-harms/
    image-resizing-tips-every-coder-should-know/
    """
    name, ext = os.path.splitext(os.path.basename(img_path))
    name = ".".join([name, "thumbnail"])
    thumb = Image.open(img_path)
    thumb.thumbnail(step_size, Image.ANTIALIAS)
    thumb.thumbnail(max_size, Image.ANTIALIAS)
    thumb_path = os.path.join(TUMB_PATH, name)
    #thumb.save(thumb_path, "JPEG", quality=80)
    #return thumb_path
    return pil_to_qimage(thumb)


def thumbnail2(img_path):
    name, ext = os.path.splitext(os.path.basename(img_path))
    name = ".".join([name, "thumbnail"])
    thumb_path = os.path.join(TUMB_PATH, name)
    resize_and_crop(img_path, thumb_path, max_size)
    return thumb_path


def resize_and_crop(img_path, modified_path, size, crop_type='top'):
    """
    Resize and crop an image to fit the specified size.
    args:
        img_path: path for the image to resize.
        modified_path: path to store the modified image.
        size: `(width, height)` tuple.
        crop_type: can be 'top', 'middle' or 'bottom', depending on this
            value, the image will cropped getting the 'top/left', 'midle' or
            'bottom/rigth' of the image to fit the size.
    raises:
        Exception: if can not open the file in img_path of there is problems
            to save the image.
        ValueError: if an invalid `crop_type` is provided.
    **Stolen of:**
    https://gist.github.com/sigilioso/2957026
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically
    #or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize(
            (size[0], size[0] * img.size[1] / img.size[0]),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
            box = (
                0,
                (img.size[1] - size[1]) / 2, img.size[0],
                (img.size[1] + size[1]) / 2)
        elif crop_type == 'bottom':
            box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else:
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize(
            (size[1] * img.size[0] / img.size[1], size[1]),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
            box = (
                (img.size[0] - size[0]) / 2, 0,
                (img.size[0] + size[0]) / 2,
                img.size[1])
        elif crop_type == 'bottom':
            box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else:
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else:
        img = img.resize(
            (size[0], size[1]),
            Image.ANTIALIAS)
        # If the scale is the same, we do not need to crop
    img.save(modified_path, "JPEG", quality=80)
