import streamlit as st
import yt_dlp
import os
import tempfile
import re

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

# Função para limpar o nome do arquivo
def limpar_nome_arquivo(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)

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
                info_dict = ydl.extract_info(url, download=True)
                video_title = info_dict.get('title', None)
                video_ext = info_dict.get('ext', None)
                
                # Limpa o nome do arquivo
                video_file_name = f"{limpar_nome_arquivo(video_title)}.{video_ext}"

                # Verifica o diretório temporário e encontra o arquivo baixado
                for file in os.listdir(tmp_dir):
                    if file == video_file_name:
                        video_path = os.path.join(tmp_dir, file)
                        # Fornece um link para download do arquivo
                        with open(video_path, "rb") as file_data:
                            st.download_button(
                                label="Clique aqui para baixar o vídeo",
                                data=file_data,
                                file_name=video_file_name,
                                mime="video/mp4"
                            )
                        st.success("Download concluído!")
                        return  # Encerra a função após o download
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
