import requests
while True:
    print("==============Consulta GitHub=================")
    username = input("Qual é o nome do usuário: ")

    url = f'https://api.github.com/users/{username}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Usuário: ", data['login'])
        print("Nome: ", data['name'])
        print("Bio: ", data['bio'])
        print("Email: ", data['email'])
        print("Followers: ", data['followers'])
        print("Following: ", data['following'])
        print("Repositórios: ", data['public_repos'])
        print("Data de criação: ", data['created_at'])
        print("Localização: ", data['location'])
    elif response.status_code == 404:
        print("Erro na consulta. Usuário não encontrado.")
    else:
        print("Erro na consulta. Código de status:", response.status_code)
    continua = input("Deseja realizar outra consulta? S/s ")
    if continua.lower() != "s":
        break