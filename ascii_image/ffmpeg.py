#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# @author   Solomon Ng <solomon.wzs@gmail.com>
# @date     2022-10-11
# @version  1.0
# @license  MIT

import os
from subprocess import Popen, PIPE, STDOUT, run


def vdo2frames(
    vdo_path: str, output_dir: str, fps: int = 10, name: str = "frame%08d.png"
) -> list[str] | None:
    cmd = f"ffmpeg -i {vdo_path} -vf fps={fps} {output_dir}/{name}"
    r = run(
        cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True
    )
    if r.returncode != 0:
        return None

    files = [os.path.join(output_dir, fn) for fn in os.listdir(output_dir)]
    files.sort()
    return files


if __name__ == "__main__":
    print(vdo2frames("/tmp/ff/HbWsr.gif", "/tmp/ff/frames"))
