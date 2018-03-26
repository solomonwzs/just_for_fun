#!/usr/bin/python3
# encoding: utf-8

import argparse
import os
import shutil
import signal
import sys
import time

from convert import image2ascii
from ffmpeg import vdo2frames


def get_workspace(tmp):
    return os.path.join(tmp, "play-ascii-gif-%d" % os.getpid())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="play ascii gif")
    parser.add_argument("file", type=str,
                        help="gif file")
    parser.add_argument("-f", "--fps", type=int, default=10,
                        help="fps (default: 10)")
    parser.add_argument("-t", "--tmp", type=str, default="/tmp",
                        help="directory for save tmp file (default: /tmp)")
    parser.add_argument("-m", "--mode", type=str, default="ascii",
                        help="ascii or color (default: ascii)")
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

    def clean(sig, frame):
        shutil.rmtree(ws)
        sys.exit(0)

    signal.signal(signal.SIGINT, clean)

    img_frames = vdo2frames(args.file, ws, args.fps)
    ascii_frames = [image2ascii(f, mode=args.mode) for f in img_frames]

    nframes = len(ascii_frames)
    i = 0
    while True:
        if i == nframes:
            i = 0
        os.system("clear")
        print(ascii_frames[i])
        i += 1

        time.sleep(1/args.fps)
    shutil.rmtree(ws)
