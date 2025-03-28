import requests

def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url).json()
    usuario = resposta["results"][0]
    print(f"Nome: {usuario['name']['first']} {usuario['name']['last']}")
    print(f"Email: {usuario['email']}")
    print(f"País: {usuario['location']['country']}")
    
gerar_perfil_usuario()