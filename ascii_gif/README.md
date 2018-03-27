# Play Ascii Gif

## Depends
+ ffmpeg
+ python-pillow


## Usage
```
usage: play.py [-h] [-f FPS] [-t TMP] [-m MODE] [-w WIDTH] [-a ACCURACY] file

play ascii gif

positional arguments:
  file                  gif file

optional arguments:
  -h, --help            show this help message and exit
  -f FPS, --fps FPS     fps (default: 10)
  -t TMP, --tmp TMP     directory for save tmp file (default: /tmp)
  -m MODE, --mode MODE  ascii or color (default: ascii)
  -w WIDTH, --width WIDTH
                        width (default: 120)
  -a ACCURACY, --accuracy ACCURACY
                        accuracy, 5-16 (default: 8)
```

## Example
```
% python3 play.py fun.gif
```
