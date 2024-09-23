# Downloader de Vídeo e Áudio com Interface Gráfica

Este script Python oferece uma interface gráfica do usuário (GUI) para baixar vídeos, extrair áudio e mesclar ambos em um único arquivo MP4.

## Funcionalidades

- **Baixar Vídeos:** Baixa vídeos do YouTube e de outras plataformas compatíveis com yt-dlp.
- **Extrair Áudio:** Extrai o áudio do vídeo baixado.
- **Mesclar Vídeo e Áudio:** Combina o vídeo e o áudio extraído em um único arquivo MP4.
- **Interface Gráfica Amigável:** Permite que os usuários insiram facilmente a URL do vídeo, escolham o nome do arquivo de saída e acompanhem o progresso do download e da mesclagem.
- **Opção de Remover Arquivos Separados:** Permite a exclusão dos arquivos de áudio e vídeo individuais após a mesclagem, mantendo apenas o arquivo MP4 final.

## Pré-requisitos

- **Python 3:** Certifique-se de ter o Python 3 instalado em seu sistema.
- **Bibliotecas:** Instale as bibliotecas necessárias:
  ```bash
  pip install yt-dlp tkinter ffmpeg-python
  ```
- **ffmpeg:** Baixe e instale o ffmpeg em [https://ffmpeg.org/](https://ffmpeg.org/) e certifique-se de que ele esteja adicionado à variável de ambiente PATH do seu sistema. Isso permitirá que o script execute o ffmpeg a partir da linha de comando.

## Como Usar

1. **Executar o Script:** Execute o script Python. Uma janela da interface gráfica será aberta.
2. **Inserir URL:** Cole a URL do vídeo desejado no campo "URL do Vídeo".
3. **Nome do Arquivo de Saída (Opcional):** Insira um nome para o arquivo de saída no campo "Nome do Arquivo Final". Se este campo for deixado em branco, o nome padrão "video_with_audio.mp4" será usado.
4. **Manter Arquivos Separados (Opcional):** Marque a caixa de seleção "Manter arquivos de vídeo e áudio separados" se desejar manter os arquivos de vídeo e áudio baixados separadamente, além do arquivo MP4 mesclado.
5. **Baixar e Mesclar:** Clique no botão "Baixar e Combinar".
6. **Selecionar Pasta de Destino:** Uma janela de diálogo será aberta para que você escolha a pasta onde deseja salvar o vídeo e o áudio.
7. **Aguardar o Download e a Mesclagem:** O progresso do download e da mesclagem será exibido na área de texto na parte inferior da janela.
8. **Pronto!** Uma mensagem será exibida quando o processo for concluído, informando o local onde o vídeo mesclado foi salvo.

## Observações

- O script usa o yt-dlp para baixar vídeos e o ffmpeg para mesclar o vídeo e o áudio.
- Certifique-se de que o ffmpeg esteja instalado corretamente e adicionado à variável de ambiente PATH do seu sistema.
- O tempo de download e mesclagem pode variar dependendo do tamanho do vídeo e da velocidade da sua internet.

EN-US

# Video and Audio Downloader with Graphical Interface

This Python script provides a graphical user interface (GUI) for downloading videos, extracting audio, and merging them into a single MP4 file.

## Features

- **Download Videos:** Downloads videos from YouTube and other platforms supported by yt-dlp.
- **Extract Audio:** Extracts the audio from the downloaded video.
- **Merge Video and Audio:** Merges the extracted video and audio into a single MP4 file.
- **User-Friendly GUI:** Allows users to easily enter the video URL, choose the output file name, and track the download and merging progress.
- **Option to Remove Separate Files:** Enables the deletion of the individual audio and video files after merging, keeping only the final MP4 file.

## Prerequisites

- **Python 3:** Make sure you have Python 3 installed on your system.
- **Libraries:** Install the necessary libraries:
  ```bash
  pip install yt-dlp tkinter ffmpeg-python
  ```
- **ffmpeg:** Download and install ffmpeg from [https://ffmpeg.org/](https://ffmpeg.org/) and ensure it is added to your system's PATH environment variable. This will allow the script to execute ffmpeg from the command line.

## How to Use

1. **Run the Script:** Execute the Python script. A graphical interface window will open.
2. **Enter URL:** Paste the URL of the desired video into the "Video URL" field.
3. **Output File Name (Optional):** Enter a name for the output file in the "Final File Name" field. If this field is left blank, the default name "video_with_audio.mp4" will be used.
4. **Keep Separate Files (Optional):** Check the "Keep separate video and audio files" checkbox if you want to keep the downloaded video and audio files separately, in addition to the merged MP4 file.
5. **Download and Merge:** Click the "Download and Merge" button.
6. **Select Destination Folder:** A dialog window will open for you to choose the folder where you want to save the video and audio.
7. **Wait for Download and Merge:** The download and merging progress will be displayed in the text area at the bottom of the window.
8. **Done!** A message will be displayed when the process is complete, informing you of the location where the merged video was saved.

## Notes

- The script uses yt-dlp to download videos and ffmpeg to merge the video and audio.
- Ensure that ffmpeg is installed correctly and added to your system's PATH environment variable.
- Download and merge time may vary depending on the video size and your internet speed.
