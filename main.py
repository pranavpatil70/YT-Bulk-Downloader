import os
import yt_dlp

# List of video URLs
video_urls = [
    #enter urls
]


def download_videos(urls):
    for url in urls:
        try:
            ydl_opts = {
                'format': 'best[ext=mp4]',
                'outtmpl': '%(title)s.%(ext)s',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print(f"Downloaded: {url}")
        except Exception as e:
            print(f"An error occurred while downloading {url}: {e}")

download_videos(video_urls)