# Subinline

These script automatically download English and Chinese subtitles of specific videos, then burn them directly into video using ffmpeg.

For `get_subtitle.py`, provide the youtube video link or video id as the first argument. 

`get_subtitle.py` will download English subtitle and Chinese subtitle.

Example: 

```bash
python3 ./get_subtitle.py WAeMt4vDJYk
```

For `burn_subtitle.py`, provide 3 argument: local path of the video, local path of the English subtitle (srv file), local path of the English subtitle (srv file).

Example: 

```bash
python3 burn_subtitle.py November\ Anime\ Youtube\ Video\ Challenge\ \(NATVC\ _\ NOVID\)-WAeMt4vDJYk.mkv --en_sub en_sub.srt --zh_sub zh_sub.srt
```
