import ctypes
import argparse

parser = argparse.ArgumentParser(add_help=True, prog='WallpaperChanger', description=' Change you wallpaper | By Michael Soyka ')
parser.add_argument('path',action="store", help='Path to image')

ctypes.windll.user32.SystemParametersInfoW(20, 0, parser.parse_args().path, 3)

