import requests
from bs4 import BeautifulSoup
import environs
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Carregar variáveis de ambiente a partir do arquivo .env
env = environs.Env()
env.read_env()

# Configurar a autenticação do Spotify usando OAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # Permissão para modificar playlists privadas
        redirect_uri="http://example.com",  # URI de redirecionamento após a autenticação
        client_id=env.str("SPOTIFY_ID"),  # ID do cliente Spotify definido nas variáveis de ambiente
        client_secret=env.str("SPOTIFY_SECRET"),  # Secret do cliente Spotify definido nas variáveis de ambiente
        show_dialog=True,  # Mostra a caixa de diálogo para o usuário confirmar a permissão
        cache_path="token.txt"  # Caminho para armazenar o token de autenticação
    )
)

# Obter o ID do usuário autenticado no Spotify
user_id = sp.current_user()["id"]

# Solicitar ao usuário a data desejada no formato YYYY-MM-DD
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Fazer uma requisição para a página da Billboard Hot 100 da data especificada
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=url, headers=header)

# Criar o objeto BeautifulSoup para analisar o HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Selecionar todos os elementos <h3> que contêm os nomes das músicas
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]  # Extrair o texto de cada <h3> e remover espaços extras

# Lista para armazenar as URIs das músicas encontradas no Spotify
song_uris = []
year = date.split("-")[0]  # Extrair o ano da data fornecida

# Buscar cada música no Spotify
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")  # Pesquisar a música pelo nome e ano
    print(result)  # Imprimir o resultado da busca para verificação
    try:
        # Adicionar a URI da primeira música encontrada
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # Caso a música não seja encontrada, exibir uma mensagem e continuar
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Criar uma nova playlist privada com o nome da data da Billboard Hot 100
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Adicionar todas as músicas encontradas na playlist recém-criada
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Playlist '{date} Billboard 100' created successfully!")
