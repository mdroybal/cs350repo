#---Monte Roybal---#
#---Audio_Video_DL---#

import youtube_dl
import sys

def my_download(d):
    if d['status'] == 'finished':
        print('File download complete, now converting format ......')

while True:
    opts = {
    
        'format': raw_input("\nPlease ENTER (1) for VIDEO download (2) for SONG download or (3) to EXIT: "), 
        'key': 'FFmpegExtractAudio',

    }


    if opts['format'] == '3':
        sys.exit("\n****Goodbye****\n")

    if opts['format'] == '2':
        opts['format'] = raw_input("\nWould you like to download (1) HIGHEST or (2) LOWEST quality audio: ")
    
        if opts['format'] == '1':
            opts['format'] = 'bestaudio'
    
        elif opts['format'] == '2': 
            opts['format'] = 'worstaudio' 


    elif opts['format'] == '1':
        opts['format'] = raw_input("\nWould you like to download (1) HIGHEST or (2) LOWEST quality video: ")
    
        if opts['format'] == '1':
            opts['format'] = '(bestvideo+bestaudio)' 

        elif opts['format'] == '2':
             opts['format'] = '(worstvideo+worstaudio)'


    url = raw_input("\nPlease ENTER the url of the video or song you would like to download: ")

    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])
