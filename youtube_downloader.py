import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp

def download_video():
    url = url_entry.get()
    
    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return
    
    save_path = filedialog.askdirectory()
    
    if not save_path:
        messagebox.showerror("Erro", "Por favor, selecione um caminho para salvar.")
        return
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'noplaylist': True,  # Baixar apenas o vídeo e não a playlist
        'age_limit': 100,  # Tentar contornar restrições de idade
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", f"Download concluído! Vídeo salvo em: {save_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("YouTube Downloader")

# Rótulo e entrada para a URL do vídeo
url_label = tk.Label(root, text="URL do Vídeo:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botão de download
download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

# Iniciar o loop principal da interface gráfica
root.mainloop()
