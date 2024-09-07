# Script for Downloading and Combining YouTube Video and Audio

This script uses the `yt-dlp` library to download videos and audio from YouTube, and then combines the video and audio using `ffmpeg`. The result is a video file with integrated audio.

## Requirements

Before running the script, ensure you have the following software installed:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (a tool for downloading videos from YouTube)
- [ffmpeg](https://ffmpeg.org/download.html) (a tool for audio and video processing)

## Installation

1. **Install `yt-dlp`**:

   ```bash
   pip install yt-dlp
   ```

2. **Install `ffmpeg`**:

   - Follow the instructions for your operating system on the [FFmpeg download page](https://ffmpeg.org/download.html).

## Usage

1. **Edit the Script**:

   - Replace the value of `url` with the URL of the YouTube video you want to download.
   - Adjust the `path` variable to specify the directory where you want to save the files.

2. **Run the Script**:

   Save the script in a file named `download_and_combine.py` and run it with:

   ```bash
   python download_and_combine.py
   ```

3. **Check the Result**:

   After running the script, you will find the combined file `video_with_audio.mp4` in the specified directory. The script also saves the video and audio separately before combining them.

PT-BR

# Script para Baixar e Combinar Vídeo e Áudio do YouTube

Este script utiliza a biblioteca `yt-dlp` para baixar vídeos e áudios do YouTube e, em seguida, combina o vídeo e o áudio usando `ffmpeg`. O resultado é um arquivo de vídeo com áudio integrado.

## Requisitos

Antes de executar o script, certifique-se de ter os seguintes softwares instalados:

- [Python](https://www.python.org/downloads/) (versão 3.6 ou superior)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (uma ferramenta para baixar vídeos do YouTube)
- [ffmpeg](https://ffmpeg.org/download.html) (uma ferramenta para manipulação de áudio e vídeo)

## Instalação

1. **Instale `yt-dlp`**:

   ```bash
   pip install yt-dlp
   ```

2. **Instale `ffmpeg`**:

   - Siga as instruções específicas para seu sistema operacional na [página de download do FFmpeg](https://ffmpeg.org/download.html).

## Como Usar

1. **Edite o Script**:

   - Substitua o valor de `url` com o URL do vídeo do YouTube que você deseja baixar.
   - Ajuste o caminho `path` para o diretório onde você deseja salvar os arquivos.

2. **Execute o Script**:

   Salve o script em um arquivo chamado `download_and_combine.py` e execute-o com:

   ```bash
   python download_and_combine.py
   ```

3. **Verifique o Resultado**:

   Após a execução, você encontrará o arquivo combinado `video_with_audio.mp4` no diretório especificado. O script também salva o vídeo e o áudio separadamente antes de combiná-los.
