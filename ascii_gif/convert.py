#!/usr/bin/python3
# encoding: utf-8

import math
from PIL import Image


ASCII_CHARS = ['M', '%', '*', ' ',
               'S', '+', '=', 'o',
               ':', '7', '|', '-',
               'x', ':', '.', '>']
COLOR_CHARS = [
    "\033[40m \033[0m",
    "\033[41m \033[0m",
    "\033[42m \033[0m",
    "\033[43m \033[0m",
    "\033[44m \033[0m",
    "\033[45m \033[0m",
    "\033[46m \033[0m",
    "\033[47m \033[0m",
]


def resize_image(image, new_width=100, rate=1.0):
    ori_width, ori_height = image.size
    aspect_ratio = ori_height / ori_width
    new_height = int(new_width * aspect_ratio * rate)

    new_image = image.resize((new_width, new_height))
    return new_image


def pixels2int(image, accuracy):
    range_width = math.ceil(0xff / accuracy)
    pixels_in_image = list(image.getdata())
    pixels_to_int = [int(pixel_value / range_width)
                     for pixel_value in pixels_in_image]
    return pixels_to_int


def image2ascii(image_path, new_width=120, mode="ascii", accuracy=8):
    image = None
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)

    if mode != "ascii":
        accuracy = 8
    else:
        if accuracy < 5:
            accuracy = 5
        elif accuracy > 16:
            accuracy = 16

    image = resize_image(image, new_width, 0.5)
    image = image.convert('L')

    ilist = pixels2int(image, accuracy)
    d = ASCII_CHARS if mode == "ascii" else COLOR_CHARS
    ascii_rows = [''.join(
        [d[i] for i in ilist[index: index + new_width]])
        for index in range(0, len(ilist), new_width)]
    return '\n'.join(ascii_rows)


if __name__ == "__main__":
    import sys
    print(image2ascii(sys.argv[1], accuracy=7))
