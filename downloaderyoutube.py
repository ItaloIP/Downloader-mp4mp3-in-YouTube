#Instale o PYTUBE e MOVIEPY!!
# PIP Install pytube
# PIP Install moviepy
from pytube import YouTube
import moviepy.editor as mp
import re
import os

#Função MP3
def MP3(url):
    path = str('Download')
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print('-='*20)
    print('Download!')
    print('-='*20)
    print('Converting for MP3')
    print('-='*20)
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] +' .mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("Finished!")
#Função MP4
def MP4(url):
    path = str('Download')
    yt = YouTube(url)
    ys = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
    print('-='*20)
    print('Download!')
    print('-='*20)


#Programa Principal
while True:
    choice = int(input('''Want to Download::
    ( 0 ) MP3
    ( 1 ) MP4
    ( 2 ) Exit
         :  '''))
    if choice == 0:
        linkk = str(input('Link (only youtube!): '))
        MP3(linkk)
        
    elif choice == 1:
        linkk = str(input('Link (only youtube!): '))
        MP4(linkk)

    elif choice == 2:
        break
    
    else:
        print('Error!')
