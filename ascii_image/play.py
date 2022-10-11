#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @author   Solomon Ng <solomon.wzs@gmail.com>
# @date     2022-10-11
# @version  1.0
# @license  MIT

import argparse
import os
import shutil
import signal
import sys
import time

from PIL import Image
from convert import image2tstr, resize_image
from ffmpeg import vdo2frames


def get_workspace(tmp):
    return os.path.join(tmp, "play-ascii-gif-%d" % os.getpid())


def imgfile2str(filename: str, width: int, ratio: float) -> tuple[int, str]:
    img = Image.open(filename)
    img = resize_image(img, width, ratio)
    img = img.convert("RGB")
    s = image2tstr(img)
    return (len(s), "\n".join(s))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="play ascii gif")
    parser.add_argument("file", type=str, help="gif file")
    parser.add_argument(
        "-f", "--fps", type=int, default=10, help="fps (default: 10)"
    )
    parser.add_argument(
        "-t",
        "--tmp",
        type=str,
        default="/tmp",
        help="directory for save tmp file (default: /tmp)",
    )
    parser.add_argument(
        "-w", "--width", type=int, default=120, help="width (default: 120)"
    )
    parser.add_argument(
        "-r",
        "--ratio",
        type=float,
        default=1.0,
        help="height ratio (default: 1.0)",
    )
    args = parser.parse_args()

    if os.path.exists(args.tmp):
        if not os.path.isdir(args.tmp):
            print(f"{args.tmp} is not dir")
            sys.exit(1)
        else:
            ws = get_workspace(args.tmp)
            os.mkdir(ws)
    else:
        print(f"{args.tmp} is not exist")
        sys.exit(1)

    def clean(si, frame):
        shutil.rmtree(ws)
        sys.exit(0)

    signal.signal(signal.SIGINT, clean)

    img_frames = vdo2frames(args.file, ws, args.fps)
    if img_frames is None:
        print("ffmpeg error")
        shutil.rmtree(ws)
        sys.exit(-1)

    ascii_frames = [imgfile2str(f, args.width, args.ratio) for f in img_frames]
    nframes = len(ascii_frames)
    i = 0
    while True:
        print(ascii_frames[i % nframes][1])
        time.sleep(1 / args.fps)
        n = ascii_frames[i % nframes][0] + 1
        print(f"\x1B[{n}F")
        i += 1
