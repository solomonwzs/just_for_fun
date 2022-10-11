# Play Ascii Gif

## Depends
+ ffmpeg
+ python-pillow


## Usage
```
usage: play.py [-h] [-f FPS] [-t TMP] [-w WIDTH] [-r RATIO] file

play ascii gif

positional arguments:
  file                  gif file

options:
  -h, --help            show this help message and exit
  -f FPS, --fps FPS     fps (default: 10)
  -t TMP, --tmp TMP     directory for save tmp file (default: /tmp)
  -w WIDTH, --width WIDTH
                        width (default: 120)
  -r RATIO, --ratio RATIO
                        height ratio (default: 1.0)
```

## Example
```
% python3 play.py fun.gif
```
