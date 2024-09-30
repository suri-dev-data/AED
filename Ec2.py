def SomaConjunto(memo, x):

    valor = 0
    for i in range(0, 21):
        soma = valor + (20-i)
        if soma <= x:
            valor += (20-i)

    if valor == x:
        print("Existe")
    else:
        print("Nao Existe")


def criaM(matriz, x):
    for i in range(0, x):
        linha = [0]*x
        matriz[i] = linha


x = int(input("O valor de x: "))
memo = [0]*x
criaM(memo, x)
SomaConjunto(memo, x)
