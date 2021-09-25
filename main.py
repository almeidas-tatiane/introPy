

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




