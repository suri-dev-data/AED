import math


def ApProva(memoT, v, t, tam, nota):
    v1 = []
    t1 = []
    for i in range(tam):
        v1.append(v[i])
        t1.append(t[i])
    for j in range(1, nota+1):
        for k in range(0, tam):
            if (j-v1[k]-1) >= 0 and k <= 5:
                memoT[j-1] = min(memoT[j-1], t[k] + memoT[j-v[k]-1])
                ind = k
            elif j-v1[k] == 0:
                memoT[j-1] = min(memoT[j-1], t[k])
                for i in range(tam):
                    v1[i] = v[i]
                    t1[i] = t[i]
                ind = k
        v1[ind] = math.inf
        t1[ind] = math.inf
        for i in range(tam):
            v1[i] = v[i]
            t1[i] = t[i]

    print(f"A quantidade de tempo e : {memoT[nota-1]}")


vNota = [1, 2, 3, 1, 2, 1]
vTempo = [4, 6, 3, 5, 1, 3]
tam = int(input("A quantidade de questoes e: "))
nota = int(input("A nota requerida e: "))
memo = [math.inf for i in range(nota+1)]
ApProva(memo, vNota, vTempo, tam, nota)
