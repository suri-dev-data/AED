from math import floor


def QuantF(m, i, f):
    quant = 0
    if (i == f):
        if (m[i] == 'F'):
            return 1
    if (i+1 == f):
        for a in range(i, f+1):
            if (m[a] == 'F'):
                quant += 1
        return quant
    else:
        med = floor((i+f)/2)
        quant += QuantF(m, i, med)
        quant += QuantF(m, med+1, f)
        return quant


m = ["V", "V", "F", "F", "V", "V", "V", "F", "F"]
tam = len(m)-1
quant = QuantF(m, 0, tam)
print("A quantidade de F's é ", quant)
