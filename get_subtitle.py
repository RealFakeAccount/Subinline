from srt import Subtitle, compose
import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import timedelta
import srt
import argparse

parser = argparse.ArgumentParser(description="fetch youtube video subtitles", epilog= \
'''This script intend to fetch the English and Chinese subtitle from specific youtube video. 
If target video has both manually and auto-generate subtitle, it will  always picks manually created transcripts over automatically created ones.
If target video's subtitle is disabled, this script will return an error.  

Example: python3 ./get_subtitle.py WAeMt4vDJYk
''')

parser.add_argument('videolink', type=str, help="Full youtube video link or video ID.")

args = parser.parse_args()

def convert_to_srt(json_sub:str):
    print("converting to srt file...")
    srt_list = []

    for i in range(len(json_sub)):
        cur = Subtitle(index=i + 1, 
        start=timedelta(seconds=json_sub[i]['start']), 
        end=timedelta(seconds=json_sub[i]['start'] + json_sub[i]['duration'] if i + 1 == len(json_sub) else 
        min(json_sub[i + 1]['start'], json_sub[i]['start'] + json_sub[i]['duration'])),
        content=json_sub[i]['text'])
        srt_list.append(cur)

    return compose(srt_list)
    ...

def main():
    video_id = args.videolink if args.videolink.find("youtube.com") == -1 else args.videolink[args.videolink.find("?v=") + 3:]
    print("find the subtitle of video:" + video_id)
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    
    eng_trans, zh_trans = None, None

    try:
        eng_trans = transcript_list.find_transcript(['en'])
    except youtube_transcript_api._errors.NoTranscriptFound:
        raise Exception("manually or automatically generated English subtitle not found. Stopped.")
    try:
        zh_trans = transcript_list.find_transcript(['zh-Hans'])
    except youtube_transcript_api._errors.NoTranscriptFound:
        print("manually or automatically generated Chinese subtitle not found. Finding translated Chinese subtitle...")
        if {'language': 'Chinese (Simplified)', 'language_code': 'zh-Hans'} not in eng_trans.translation_languages:
            print("Chinses subtitle can nither be generated nor translated. Download English subtitle only.")
        else: zh_trans = eng_trans.translate('zh-Hans')

    with open("en_sub.txt", 'w') as f:
        print(convert_to_srt(eng_trans.fetch()), file=f)

    if zh_trans:
        with open("zh_sub.txt", 'w') as f:
            print(convert_to_srt(zh_trans.fetch()), file=f)
    ...



if __name__ == '__main__':
    main()