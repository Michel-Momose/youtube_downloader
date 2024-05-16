from pytube import YouTube


def download_youtube_video(url, save_path):
    try:
        # Cria um objeto YouTube
        yt = YouTube(url)

        # Seleciona a stream de vídeo com a maior resolução disponível
        stream = yt.streams.get_highest_resolution()

        # Baixa o vídeo para o caminho especificado
        stream.download(output_path=save_path)

        print(f"Download concluído! Vídeo salvo em: {save_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # URL do vídeo do YouTube
    video_url = input("Digite a URL do vídeo do YouTube: ")

    # Caminho para salvar o vídeo baixado
    save_path = input("Digite o caminho para salvar o vídeo (exemplo: C:/Users/SeuUsuario/Videos): ")

    download_youtube_video(video_url, save_path)