
def criaVet(texto, padrao):
    pad = []
    vetor = []
    for j in range(0, len(padrao)):
        if (padrao[j] != " "):
            pad.append(padrao[j])
    for a in range(0, len(texto)):
        for i in range(0, len(pad)):
            if (texto[a] == pad[i]):
                vetor.append(texto[a])
    return vetor


def AchaPadrao(num, vetor, padrao):
    pad = []
    cont = 0
    for j in range(0, len(padrao)):
        if (padrao[j] != " "):
            pad.append(padrao[j])
    for i in range(0, len(vetor)):
        if (vetor[i] == pad[0]):
            cont1 = 0
            for j in range(0, len(pad)):
                if (vetor[i+j] == pad[j]):
                    cont1 += 1
                else:
                    cont1 = 0
            if (cont1 == len(pad)):
                cont += 1

    if (cont == num):
        return 1
    return 0


num = int(input("Numero de Repeticoes: "))
texto = input("Texto:")
padrao = input("O padrão:")
vetor = criaVet(texto, padrao)

if (AchaPadrao(num, vetor, padrao)):
    print("Y")
else:
    print("F")
