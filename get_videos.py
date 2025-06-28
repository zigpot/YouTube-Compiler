from pytube import Playlist
import yt_dlp
import os

#playlist = Playlist('https://www.youtube.com/playlist?list=PLREQ8S3NPaQt3JX33DN0QdGgtBJtAcTYQ')
#video_urls = list(playlist.video_urls)

video_urls = []
with open("list", "r", encoding="utf-8") as f:
    video_urls = [line.strip() for line in f if line.strip()]

def srt_to_txt(srt_file):
    with open(srt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    text = ' '.join(
        line.strip() for line in lines
        if not line.strip().isdigit() and '-->' not in line and line.strip()
    )
    txt_file = srt_file.replace('.en.srt', '.txt')
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(text)
    os.remove(srt_file)  # delete original .srt

ydl_opts = {
    'skip_download': True,
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en'],
    'subtitlesformat': 'srt',
    'outtmpl': './rom/%(title)s.%(ext)s',

}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in video_urls:
        try:
            info = ydl.extract_info(url, download=True)
            title = info.get('title')
            srt_file = f"./{title}.srt"
            if os.path.exists(srt_file):
                srt_to_txt(srt_file)
                print(f"Saved: {title}.txt")
            else:
                print(f"No English auto-caption for: {srt_file}")
        except Exception as e:
            print(f"Error processing {url}: {e}")

