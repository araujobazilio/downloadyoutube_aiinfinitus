# Downloader de Vídeo do YouTube

Este é um aplicativo simples desenvolvido em Python usando Streamlit e yt-dlp, que permite aos usuários baixar vídeos do YouTube diretamente para o seu computador.

## Funcionalidades

- **Download de Vídeos**: Insira a URL de um vídeo do YouTube e baixe-o diretamente.
- **Barra de Progresso**: Visualize o progresso do download em tempo real com uma barra de progresso que vai de 0% a 100%.
- **Link de Download**: Após o download, um link é fornecido para que o usuário possa baixar o vídeo.

## Pré-requisitos

Antes de executar o aplicativo, você precisa ter o Python instalado em seu sistema. Você também precisará instalar as bibliotecas necessárias.

### Instalação do Python

Você pode baixar o Python em [python.org](https://www.python.org/downloads/).

### Instalação das Dependências

1. Clone este repositório ou baixe o código-fonte.
2. Navegue até o diretório do projeto no terminal.
3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências necessárias:

   ```bash
   pip install streamlit yt-dlp
   ```

## Como Executar o Aplicativo

1. No terminal, navegue até o diretório onde o arquivo `app.py` está localizado.
2. Execute o seguinte comando:

   ```bash
   streamlit run app.py
   ```

3. O aplicativo será iniciado e você poderá acessá-lo no seu navegador em `http://localhost:8501`.

## Como Usar

1. Abra o aplicativo no seu navegador.
2. Insira a URL do vídeo do YouTube que deseja baixar.
3. Clique no botão "Baixar Vídeo".
4. Acompanhe o progresso do download na barra de progresso.
5. Após a conclusão, um botão será exibido para baixar o vídeo.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.