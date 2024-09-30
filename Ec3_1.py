

v = [0 for i in range(0, 3)]


def permute(cont, list, limit, s):
    if (s > 0):
        for i in range(0, 100):
            v[cont][abs(s-3)] = list[i]
            if (s == 1):
                print(v[cont])
            permute(cont, list, limit, s-1)


cont = 0
list = [i for i in range(1, 500)]
permute(cont, list, 100, 3)
