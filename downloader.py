import yt_dlp
import os
import glob
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import subprocess
import sys
import re


class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.text_widget.update_idletasks()

    def flush(self):
        pass


def progress_hook(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str']
        update_status(f"Download: {percentage}")


def download_video():
    url = url_entry.get()
    output_name = output_name_entry.get()
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira a URL do vídeo.")
        return

    path = filedialog.askdirectory(title="Selecione a pasta para salvar o vídeo e o áudio")
    if not path:
        messagebox.showwarning("Aviso", "Por favor, selecione uma pasta.")
        return

    # Configuração para baixar o vídeo
    video_opts = {
        'format': 'bestvideo',
        'outtmpl': os.path.join(path, 'video.%(ext)s'),
        'progress_hooks': [progress_hook],
    }

    # Configuração para baixar o áudio
    audio_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(path, 'audio.%(ext)s'),
        'progress_hooks': [progress_hook],
    }

    try:
        print("Baixando vídeo...")

        with yt_dlp.YoutubeDL(video_opts) as ydl:
            ydl.download([url])

        print("Baixando áudio...")

        with yt_dlp.YoutubeDL(audio_opts) as ydl:
            ydl.download([url])

        # Localizar os arquivos baixados
        video_file = glob.glob(os.path.join(path, 'video.*'))[0]  
        audio_file = glob.glob(os.path.join(path, 'audio.*'))[0]  

       
        output_file = os.path.join(path, f'{output_name or "video_with_audio"}.mp4')

        print("Combinando vídeo e áudio...")
        command = [
            'ffmpeg', '-i', video_file, '-i', audio_file,
            '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', output_file
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Captura e exibe a saída do ffmpeg
        for line in process.stderr:
            match = re.search(r'frame=.*time=.*?(\d+)%', line)
            if match:
                percent = match.group(1)
                update_status(f"Combinação: {percent}%")

        process.wait() 

        if process.returncode == 0:
            print(f"Vídeo combinado salvo em: {output_file}")
        else:
            print(f"Erro durante a combinação: {process.stderr.read()}")


        if not keep_files_var.get():
            os.remove(video_file)
            os.remove(audio_file)
            print("Arquivos de vídeo e áudio separados removidos.")

        messagebox.showinfo("Sucesso", f"Vídeo combinado salvo em: {output_file}")

    except Exception as e:
        print(f"Erro: {e}")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def update_status(message):
    status_text.insert(tk.END, message + "\n")
    status_text.see(tk.END)
    root.update_idletasks()


def start_download():
    download_thread = threading.Thread(target=download_video)
    download_thread.start()


root = tk.Tk()
root.title("Downloader de Vídeo e Áudio")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)


url_label = tk.Label(frame, text="URL do Vídeo:")
url_label.grid(row=0, column=0, sticky="w")

url_entry = tk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)


output_name_label = tk.Label(frame, text="Nome do Arquivo Final:")
output_name_label.grid(row=1, column=0, sticky="w")

output_name_entry = tk.Entry(frame, width=50)
output_name_entry.grid(row=1, column=1, padx=5, pady=5)


keep_files_var = tk.BooleanVar(value=False)
keep_files_check = tk.Checkbutton(frame, text="Manter arquivos de vídeo e áudio separados", variable=keep_files_var)
keep_files_check.grid(row=2, columnspan=2, pady=5)


download_button = tk.Button(frame, text="Baixar e Combinar", command=start_download, bg="blue", fg="white")
download_button.grid(row=3, columnspan=2, pady=10)


status_text = scrolledtext.ScrolledText(frame, width=60, height=10, state='normal')
status_text.grid(row=4, columnspan=2, pady=10)


sys.stdout = RedirectText(status_text)
sys.stderr = RedirectText(status_text)


root.mainloop()
