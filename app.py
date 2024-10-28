import streamlit as st
import yt_dlp
import os
import tempfile

# Função para exibir o progresso
def progresso(status):
    downloaded = status.get('downloaded_bytes', 0)
    total = status.get('total_bytes', 1)
    if total > 0:
        percentage = downloaded / total * 100
        st.session_state.progress_bar.progress(int(percentage))  # Atualiza a barra de progresso
        st.session_state.progress_text.text(f"Progresso: {int(percentage)}%")
    if status['status'] == 'finished':
        st.session_state.progress_text.text("Download concluído!")  # Mensagem de conclusão

# Função para baixar o vídeo do YouTube
def baixar_video(url):
    # Cria um diretório temporário para o download
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_path = os.path.join(tmp_dir, "%(title)s.%(ext)s")

        ydl_opts = {
            'format': 'best',
            'outtmpl': output_path,
            'progress_hooks': [progresso],  # Atualiza o progresso
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                st.write("Iniciando o download...")
                ydl.download([url])
                
                # Listar todos os arquivos no diretório temporário
                arquivos_baixados = os.listdir(tmp_dir)
                if arquivos_baixados:
                    video_path = os.path.join(tmp_dir, arquivos_baixados[0])
                    
                    # Fornece um link para download do arquivo
                    with open(video_path, "rb") as file_data:
                        st.download_button(
                            label="Clique aqui para baixar o vídeo",
                            data=file_data,
                            file_name=arquivos_baixados[0],
                            mime="video/mp4"
                        )
                    st.success("Download concluído!")
                else:
                    st.error("O arquivo de vídeo não foi encontrado após o download.")
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")

# Interface do Streamlit
st.title("Downloader de Vídeo do YouTube")
st.text("Digite a URL do vídeo do YouTube abaixo:")
url = st.text_input("URL do vídeo do YouTube:")

# Inicializa a barra de progresso e o texto de progresso
if 'progress_bar' not in st.session_state:
    st.session_state.progress_bar = st.progress(0)
if 'progress_text' not in st.session_state:
    st.session_state.progress_text = st.empty()

if st.button("Baixar Vídeo"):
    if url:
        st.write("Iniciando o processo de download...")
        st.session_state.progress_bar.progress(0)  # Reseta a barra de progresso
        st.session_state.progress_text.text("Progresso: 0%")  # Reseta o texto de progresso
        baixar_video(url)
    else:
        st.warning("Por favor, insira uma URL válida.")
