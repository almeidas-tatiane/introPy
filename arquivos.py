#1- importação de pacotes
import json
import pytest

#2 - Classe (opcional no Python)

#3- Definições (Funções e Métodos)
dados = {}

dados['clientes'] = [] #indica a criação de um vetor, matriz, lista...
dados['clientes'].append({
    'nome': 'Juca',
    'telefone': '11999999999',
    'email': 'juca@iterasys.com.br'
     })
dados['clientes'].append({
    'nome': 'Ana',
    'telefone': '21888888888',
    'email': 'ana@iterasys.com.br'
     })

def criar_json():
    with open('clientes.json','w') as outfile:
        json.dump(dados,outfile,indent=4)

def ler_json():
    with open('clientes2.json') as outfile:
        dados = json.load(outfile)
        for registro in dados['clientes']:
            print(f'nome:' + registro['nome'])
            print(f'telefone:' + registro['telefone'])
            print(f'email:' + registro['email'])
            print('')

def ler_e_adicionar_json():
    with open('clientes2.json') as outfile:
        dados2 = json.load(outfile)
        temp = []
        for registro in dados2['clientes']:
            # Exibir no console
            print('nome:' + registro['nome'])
            print('telefone:' + registro['telefone'])
            print('email:' + registro['email'])
            print('')
            # Salvar na lista
            #   'nome': 'Claudio',
            temp.append('{\'nome\'' + ':' + '\'' + registro['nome'] + '\','
                        + '\'telefone\'' + ':' + '\'' + registro['telefone'] + '\','
                        + '\'email\'' + ':' + '\'' + registro['email'] + '\'}'
                        )
        #dados['clientes'].append(temp)
        dados['clientes'].extend(temp)
        with open('clientes3.json', 'w') as outfile:
            json.dump(dados, outfile, indent=4)





def testar_criar_json():
    criar_json()
    print(dados['clientes'])

def testar_ler_json():
    print('Leitura do JSON por linha / campo')
    ler_json()
    print(dados['clientes'])

def testar_ler_e_adicionar_json():
    ler_e_adicionar_json()
    print(dados['clientes'])


