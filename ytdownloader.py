from pytube import YouTube
import os

link = YouTube(input('Insira o link do vídeo: '))
title = link.title
streams = link.streams

quality = []
for streame in streams:
    if streame.resolution not in quality:
        quality.append(streame.resolution)
quality = sorted([i for i in quality if i])

print('Baixando...')
streams.filter(only_video=True, resolution=quality[0]).first().download()
streams.filter(only_audio=True).first().download('audio')

print('Convertendo...')
os.system('ffmpeg -i "'+os.getcwd()+'\\'+title+'.mp4" -i '+os.getcwd()+'"\\audio\\'+title+'.mp4" -c:v copy -c:a aac output.mp4')
print('Download concluído!')
os.remove(title+'.mp4')
os.remove('audio/'+title+'.mp4')
os.rename(r'output.mp4', title+'.mp4')