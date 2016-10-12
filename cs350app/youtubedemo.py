import youtube_dl
import sys

def my_download(d):
    if d['status'] == 'finished':
        print('File download complete, now converting ......')

ydl_opts = {
    
    'format': raw_input("Enter (1) to download a video or (2) to download a song: "), 
    'key': 'FFmpegExtractAudio',

}

if ydl_opts['format'] == '1':
    ydl_opts['format'] = 'mp4'
    
elif ydl_opts['format'] == '2':
    ydl_opts['format'] = 'bestaudio/best'

while True:
    url = raw_input("\nPlease enter a url to a video or song you would like to download(Enter -1 to quit): ")
    
    if url == 1:           
        sys.exit("Goodbye")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
