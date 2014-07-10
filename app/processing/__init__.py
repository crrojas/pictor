from thumbnail import thumbnail, thumbnail2
from PIL import Image


def is_image(img_path):
    """
    Verify if a given file is a valid Image.
    Improve this method!!!!!
    """
    try:
        img = Image.open(img_path)
        return True
    except IOError:
        return False
