#!/usr/bin/python3
# encoding: utf-8

from PIL import Image


# ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
ASCII_CHARS = ['-', '|', '%', '.', 'S', '+']
COLOR_CHARS = [
    "\033[30m#\033[0m",
    "\033[31m#\033[0m",
    "\033[32m#\033[0m",
    "\033[33m#\033[0m",
    "\033[34m#\033[0m",
    "\033[35m#\033[0m",
    "\033[36m#\033[0m",
    "\033[37m#\033[0m",
]


def resize_image(image, new_width=100, rate=1.0):
    ori_width, ori_height = image.size
    aspect_ratio = ori_height / ori_width
    new_height = int(new_width * aspect_ratio * rate)

    new_image = image.resize((new_width, new_height))
    return new_image


def pixels2int(image, range_width=50):
    pixels_in_image = list(image.getdata())
    pixels_to_int = [int(pixel_value / range_width)
                     for pixel_value in pixels_in_image]
    return pixels_to_int


def image2ascii(image_path, new_width=120, mode="ascii"):
    image = None
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)

    image = resize_image(image, new_width, 0.5)
    image = image.convert('L')

    ilist = pixels2int(image)
    d = ASCII_CHARS if mode == "ascii" else COLOR_CHARS
    ascii_rows = [''.join(
        [d[i] for i in ilist[index: index + new_width]])
        for index in range(0, len(ilist), new_width)]
    return '\n'.join(ascii_rows)


if __name__ == "__main__":
    import sys
    print(image2ascii(sys.argv[1]))
