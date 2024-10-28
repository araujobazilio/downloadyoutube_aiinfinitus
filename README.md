YouTube Video Downloader
Este é um aplicativo em Python que permite o download de vídeos do YouTube, utilizando a biblioteca yt-dlp e a interface de usuário do Streamlit. O aplicativo está hospedado no Streamlit Cloud, permitindo que usuários baixem vídeos diretamente no navegador.

Funcionalidades
Baixa vídeos do YouTube na melhor qualidade disponível.
Exibe o progresso do download em tempo real.
Interface de usuário simples, intuitiva e responsiva com Streamlit.
Fornece um botão de download direto após a conclusão do download.
Tecnologias Utilizadas
Python: Linguagem de programação principal.
Streamlit: Framework para a criação de aplicações web de maneira rápida e interativa.
yt-dlp: Ferramenta de download para vídeos de sites como YouTube, com suporte para vários formatos.
Pré-requisitos
Para executar o projeto localmente, você precisará das seguintes bibliotecas instaladas:

bash
Copy code
pip install streamlit yt-dlp
Ou você pode adicionar essas dependências ao seu arquivo requirements.txt para facilitar o deploy no Streamlit Cloud.

requirements.txt
plaintext
Copy code
streamlit
yt-dlp
Como Executar o Projeto Localmente
Clone este repositório:

bash
Copy code
git clone https://github.com/seu_usuario/nome_do_repositorio.git
Acesse o diretório do projeto:

bash
Copy code
cd nome_do_repositorio
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Execute o aplicativo com o Streamlit:

bash
Copy code
streamlit run app.py
Abra seu navegador e acesse http://localhost:8501 para visualizar a aplicação.

Deploy no Streamlit Cloud
Este projeto pode ser facilmente hospedado no Streamlit Cloud. Siga estas etapas para o deploy:

Acesse Streamlit Cloud e faça login.
Crie um novo aplicativo e conecte-o ao repositório do GitHub onde este projeto está armazenado.
Certifique-se de que o arquivo requirements.txt está incluído para que as dependências sejam instaladas automaticamente.
Configure as variáveis e finalize o deploy. Seu aplicativo estará pronto para uso online!
Como Usar
Insira o link do vídeo do YouTube no campo de entrada.
Clique em "Baixar Vídeo".
Acompanhe o progresso do download na barra de progresso.
Após o download ser concluído, clique no botão de download para baixar o arquivo diretamente para o seu dispositivo.
Estrutura do Projeto
plaintext
Copy code
.
├── app.py               # Código principal do aplicativo
├── requirements.txt     # Lista de dependências do projeto
└── README.md            # Documentação do projeto
Observações
Diretório Temporário: No Streamlit Cloud, o arquivo é salvo em um diretório temporário e está disponível para download somente durante a sessão ativa do usuário. O arquivo será apagado após a sessão ser encerrada.
Limitações de Download: Este aplicativo está destinado ao uso pessoal e educativo. Respeite os direitos autorais e a política de uso do YouTube ao baixar conteúdos.
Contribuição
Sinta-se à vontade para contribuir com melhorias e novas funcionalidades. Faça um fork deste repositório, crie uma nova branch para sua funcionalidade e envie um pull request. Todas as contribuições são bem-vindas!