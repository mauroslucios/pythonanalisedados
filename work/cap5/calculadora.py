print('** Calculadora em Python **')
print(f'Escolha uma operação abaixo')
print('Soma = 1\nSubtração = 2\nMultiplicação = 3\nDivisão = 4\n')
opcao = int(input("Digite a operação: "))

def somar(n1,n2):
    return print(f'A soma de {n1} + {n2} = ',n1 + n2)

def subtrair(n1,n2):
    return print(f'A subtração de {n1} - {n2} = ',n1 - n2)

def multiplicar(n1,n2):
    return print(f'A multilicação de {n1} * {n2} = ',n1 * n2)

def divisao(n1,n2):
    return print(f'A divisão de {n1} / {n2} = ',n1 / n2)

if opcao == 1:
    print(f'Entre com 2 números para somar.')
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    somar(n1,n2)

elif opcao == 2:
    print(f'Entre com 2 números para subtrair.')
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    subtrair(n1,n2)

elif opcao == 3:
    print(f'Entre com 2 números para multiplicar.')
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    multiplicar(n1,n2)

elif opcao == 4:
    print(f'Entre com 2 números para dividir.')
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    divisao(n1,n2)
else:
    print(f'Você não escolheu nenhuma opção de 1 a 4.')
    print(f'Saindo da calculadora...')