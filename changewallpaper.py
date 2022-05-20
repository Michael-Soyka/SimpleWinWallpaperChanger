import ctypes
import argparse
from sys import platform

parser = argparse.ArgumentParser(add_help=True, prog='WallpaperChanger', description=' Change you wallpaper | By Michael Soyka ')
parser.add_argument('path',action="store", help='Path to image')

if platform == "win32":
    ctypes.windll.user32.SystemParametersInfoW(20, 0, parser.parse_args().path, 3)
else:
    print("Sorry, but this script only works under windows")
