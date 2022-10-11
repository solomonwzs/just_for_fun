#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @author   Solomon Ng <solomon.wzs@gmail.com>
# @date     2022-10-11
# @version  1.0
# @license  MIT

from PIL import Image
from convert import image2tstr, resize_image

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="open image")
    parser.add_argument("file", type=str, help="image file")
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=120,
        help="max disply width (default: 120)",
    )
    parser.add_argument(
        "-r",
        "--ratio",
        type=float,
        default=1.0,
        help="height ratio (default: 1.0)",
    )
    args = parser.parse_args()

    img = Image.open(args.file)
    img = resize_image(img, args.width, args.ratio)
    img = img.convert("RGB")
    s = image2tstr(img)
    for i in s:
        print(i)
