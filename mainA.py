

def print_hi(name):
    print(f'Oi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero in range(fim): #repetir o bloco de zero até o fim
        print(numero)          #exibir o numero

def apoiar_candidato(nome,vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print(f'{contador} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

def exibir_dia_da_semana_if(numero):
    if numero == 1:
        print('O dia é segunda')
    elif numero == 2:
        print('O dia é terça')
    elif numero == 3:
        print('O dia é quarta')
    elif numero == 4:
        print('O dia é quinta')
    elif numero == 5:
        print('O dia é sexta')
    elif numero == 6:
        print('O dia é sabado')
    elif numero == 7:
        print('O dia é domingo')
    else:
        print('Número de dia inválido. Digite um numero de 1 a 7')

# def exibir_dia_da_semana_match(numero):
#     match numero:
#         case 1:
#             print('O dia é segunda')
#             exit()
#         case 2:
#             print('O dia é terça')
#             exit()
#         case 3:
#             print('O dia é quarta')
#             exit()
#         case 4:
#             print('O dia é quinta')
#             exit()
#         case 5:
#             print('O dia é sexta')
#             exit()
#         case 6:
#             print('O dia é sabado')
#             exit()
#         case 7:
#             print('O dia é domingo')
#             exit()
#         case _:
#             print('Número de dia inválido. Digite um numero de 1 a 7')

def brincar_de_para_ou_continua():
    resposta = 'C'

    #while resposta == 'C' or resposta == 'c':
    while resposta.upper() == 'C':
        resposta = input('Digite C para continuar or qualquer outro caracter para continuar')

    print('Você decidiu parar com a brincadeira')


if __name__ == '__main__':
    print_hi('Tati')

#Chamar a função de calculo da area do retangulo
resultado = calcular_area_do_retangulo(3,4)
print(f'A area do retangulo e de {resultado} m²')

#Chamar a função de calculo da area do quadrado
resultado = calcular_area_do_quadrado(5)
print(f'A área do quadrado é de {resultado} m²')

#Chamar a função de calculo da area do trinagulo
resultado = calcular_area_do_triangulo(6,7)
print(f'A área do triângulo é de {resultado} m²')

#Executar uma chamada progressiva
contagem_progressiva(11)

#Exibir o nome do candidato várias vezes
apoiar_candidato('Amoedo',100)

#Brincar de PLIM
brincar_de_plim(100)

#Exemplo de dia da semana com if - elif - else
exibir_dia_da_semana_if(3)

#Exemplo de dia da semana com match - case
# exibir_dia_da_semana_match(1)

#Exemplo com while - para ou continua
brincar_de_para_ou_continua()



