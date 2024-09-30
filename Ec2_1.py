array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
soma = int(input("Digite a soma: "))
tabela = [[-1 for i in range(soma+1)] for j in range(soma+1)]
n = len(array)


def acharSoma(array, n, soma):
    if (soma == 0 or soma in array):
        return 1
    elif n < 0 or soma < 0:
        return 0
    elif tabela[n-1][soma] != -1:
        return tabela[n-1][soma]
    elif array[n-1] > soma:
        tabela[n-1][soma] = acharSoma(array, n - 1, soma)
        return tabela[n-1][soma]
    else:
        tabela[n-1][soma] = acharSoma(array, n - 1, soma)
        return tabela[n - 1][soma] or acharSoma(array, n - 1, soma - array[n-1])


if acharSoma(array, n, soma) == 1:
    print("Existe.")
else:
    print("Não existe.")
