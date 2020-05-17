import requests
from time import sleep

cabecalho = {
    'User-agent' : 'Mozilla/5.0 (X11; Linux x86_64)',
    'Referer' : 'https://google.com'
}


print('Bem-Vindo ao WebTry!')

options = '''Que ação deseja realizar? 
[ 1 ] Acessar 1 URL
[ 2 ] Acessar mais de uma URL
[ 3 ] Pegar código-fonte de uma página
[ 4 ] Sair do programa'''
print(options)
option = int(input('Opção: '))

while option != 4:
    if option == 1:
        print('Digite a URL do site que deseja checar; ')
        url = str(input('URL: '))

        try:
            req = requests.get(url)
            print(f'\033[32mOnline; status_code = {req.status_code}\033[m')
        except Exception as e:
            print(f'\033[1;31mRequisição deu erro:\033[m {e}')

    if option == 2:
        urls = []

        num_url = int(input('Quantos sites deseja checar? '))

        for c in range(0, num_url):
            url = str(input(f'URL {c}: '))
            urls.append(url)

        for url in range(0, len(urls)):
            try:
                req = requests.get(urls[url])
                print(f'\033[32mOnline; status_code = {req.status_code}\033[m')
            except Exception as e:
                print(f'\033[1;31mRequisição deu erro:\033[m {e}')

        sleep(3)

    if option == 3:
        print('Digite a URL do site que deseja obter o código-fonte; ')
        url = str(input('URL: '))

        try:
            req = requests.get(url)
            print('\033[32mCódigo-Fonte acessado com sucesso. Carregando...\033[m')
            sleep(3)
            print(req.text)

        except Exception as e:
            print(f'\033[1;31mRequisição deu erro:\033[m {e}')

    else:
        print('Ainda estamos trabalhando nesta opção.')

    print(options)
    option = int(input('Opção: '))

print('\033[31mPrograma Encerrado.')