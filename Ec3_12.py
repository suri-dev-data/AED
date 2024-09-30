

v = [0 for i in range(0, 4)]


def permute(list, limit, s):
    if (s > 0):
        for i in range(0, 100):
            test = True
            for j in range(1, 5):
                if (list[i] == v[abs(s-j)]):
                    test = False
            if test is True:
                v[abs(s-4)] = list[i]
                if (s == 1):
                    print(v)
                permute(list, limit, s-1)


cont = 0
list = [i for i in range(1, 500)]
permute(list, 100, 4)
