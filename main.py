import yt_dlp
import os

url = "https://youtu.be/MHhdluwaaQ4?si=sy-ayOOmFwE6YE_S"
path = os.path.expanduser('~/Documentos')

# Configuração para baixar o vídeo
video_opts = {
    'format': 'bestvideo',
    'outtmpl': f'{path}/video.%(ext)s',
}

# Configuração para baixar o áudio
audio_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{path}/audio.%(ext)s',
}

try:
    # Baixar vídeo
    with yt_dlp.YoutubeDL(video_opts) as ydl:
        ydl.download([url])
    
    # Baixar áudio
    with yt_dlp.YoutubeDL(audio_opts) as ydl:
        ydl.download([url])
    
    print("Downloads completos.")

    # Combine o vídeo e o áudio usando ffmpeg
    video_file = os.path.expanduser('~/Documentos/video.mp4')
    audio_file = os.path.expanduser('~/Documentos/audio.webm')
    output_file = os.path.expanduser('~/Documentos/video_with_audio.mp4')

    os.system(f'ffmpeg -i {video_file} -i {audio_file} -c:v copy -c:a aac -strict experimental {output_file}')
    print(f"Vídeo combinado salvo em: {output_file}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")