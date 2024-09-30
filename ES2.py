from typing import List

#  Implementar a versao 2 do algoritmo e apresentar a saida para 14 times.


def matriz(m):
    for i in range(0, lin):
        m.append(0)
        m[i] = []
        for j in range(0, col):
            m[i].append(0)
    return m


def torneio(m):
    if m == 1:
        Tab[0][0] = 1
        return Tab

    else:
        p = int(m//2)
        torneio(p)
        for i in range(0, p):
            for j in range(0, p):
                Tab[i+p][j] = Tab[i][j] + p
                Tab[i][j+p] = m - (j - i + m) % p
                Tab[(m - (j - i + m) % p) - 1][j+p] = i + 1
        return Tab


def adap(m):
    for i in range(0, m):
        for j in range(0, m):
            if Tab[i][j] == m:
                Tab[i][j] = 0

    return Tab


def adapt(m):
    for i in range(m-1, m):
        for j in range(0, m):
            if Tab[i][j] != 0:
                Tab[i][j] = 0

    return Tab


def adapta(m):

    for i in range(0, m-1):
        for j in range(0, m):
            if Tab[i][j] == 0:
                a = Tab[i][m-1]
                Tab[i][j] = a
                Tab[i][m-1] = 0

    return Tab


def print_matriz(m):
    for i in range(m):
        for j in range(m):
            if (Tab[i][j] != 0):
                print(Tab[i][j], end=" ")
        print("")


n = int(input('n: '))
m = n + 2
lin = m
col = m
Tab = []  # type: List[int]
matriz(Tab)


torneio(m)

adap(m)
adapta(m)
adapt(m)
adap(m-1)
adapta(m-1)
adapt(m-1)

print('Tabela Final: ')

print_matriz(m)
