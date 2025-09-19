import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pathlib import Path
import threading

# root = tk.Tk()
# root.withdraw()

# pasta_padrao = str(Path.home())

# playlist_url = simpledialog.askstring("Link da Playlist", "Cole o link da playlist do YouTube:")

# if not playlist_url:
#     print("Nenhum link fornecido. Encerrando.")
#     exit()

# pasta_destino = filedialog.askdirectory(title="Escolha a pasta onde deseja salvar as músicas", initialdir=pasta_padrao)
# if not pasta_destino:
#     print("Nenhuma pasta selecionada. Encerrando.")
#     exit()

# os.makedirs(pasta_destino, exist_ok=True)

# opcoes = {
#     'format': 'bestaudio/best',
#     'outtmpl': os.path.join(pasta_destino, '%(playlist_index)s - %(title)s.%(ext)s'),
#     'ignoreerrors': True,
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
# }

# with yt_dlp.YoutubeDL(opcoes) as ydl:
#     ydl.download([playlist_url])
   
   
   
def baixar_playlist(playlist_url, pasta_destino, status_label):
    status_label.config(text="⏳ Baixando músicas...")

    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(pasta_destino, '%(playlist_index)s - %(title)s.%(ext)s'),
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([playlist_url])
        status_label.config(text="✅ Download finalizado!")
        messagebox.showinfo("Concluído", "🎶 Músicas baixadas com sucesso!")
    except Exception as e:
        status_label.config(text="❌ Erro no download.")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def iniciar_interface():
    root = tk.Tk()
    root.title("Baixar Playlist do YouTube")
    root.geometry("500x200")

    # Label de status
    status_label = tk.Label(root, text="Pronto para baixar 🎧", font=("Arial", 12))
    status_label.pack(pady=10)

    def iniciar_download():
        playlist_url = simpledialog.askstring("Link da Playlist", "Cole o link da playlist do YouTube:", parent=root)
        if not playlist_url:
            return

        pasta_padrao = str(Path.home())
        pasta_destino = filedialog.askdirectory(title="Escolha onde salvar as músicas", initialdir=pasta_padrao)
        if not pasta_destino:
            return

        os.makedirs(pasta_destino, exist_ok=True)

        # Roda o yt-dlp em uma thread para não travar a interface
        threading.Thread(target=baixar_playlist, args=(playlist_url, pasta_destino, status_label)).start()

    # Botão de iniciar
    botao = tk.Button(root, text="Selecionar Playlist e Pasta", command=iniciar_download, font=("Arial", 14), bg="#4CAF50", fg="black")
    botao.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()