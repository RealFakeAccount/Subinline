import argparse
from argparse import PARSER
import subprocess, argparse

parser = argparse.ArgumentParser(description="burn subtitles into video", epilog= \
'''
burn English and Chinese subtitle into video. 

Example: python3 burn_subtitle.py November\ Anime\ Youtube\ Video\ Challenge\ \(NATVC\ _\ NOVID\)-WAeMt4vDJYk.mkv --en_sub en_sub.txt --zh_sub zh_sub.txt
''')

parser.add_argument('video', type = str, help="path of the video")

parser.add_argument('--en_sub', type = str, help = "path of the English sub")

parser.add_argument('--zh_sub', type = str, help = "path of the Chinese sub")

args = parser.parse_args()

def main():
    subprocess.call(["ffmpeg", "-i", args.video, 
    "-strict", "-2", "-vf", 
    "subtitles=" + args.en_sub + ":force_style='Fontsize=15\\,Fontname=FZYBKSJW--GB1-0\\PrimaryColour=&HCCFF66&\\,Bold=-1\\,BorderStyle=1'", 
    "-qscale:v", "3", "en_" + args.video])

    if args.zh_sub:
        subprocess.call(["ffmpeg", "-i", "en_" + args.video, 
        "-strict", "-2", "-vf", 
        "subtitles=" + args.zh_sub + ":force_style=:force_style='Fontsize=20\\,Fontname=FZYBKSJW--GB1-0\\,MarginV=30\\,Bold=-1\\,BorderStyle=1'", 
        "-qscale:v", "3", "en_zh_" + args.video])


if __name__ == '__main__':
    main()