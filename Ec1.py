

from math import floor


def merge(arr, co, m, r):
    n1 = int(m - co + 1)
    n2 = int(r - m)

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[co + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = co     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    # l is for left index and r is right index of the
    # sub-array of arr to be sorted


def mergeSort(arr, ini, r):
    if ini < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = floor(ini+(r-ini)//2)

        # Sort first and second halves
        mergeSort(arr, ini, m)
        mergeSort(arr, m+1, r)
        merge(arr, ini, m, r)


def Moda(m, i, f):
    if (i == f):
        return (m[i], 1)
    elif (i+1 == f):
        if (m[i] == m[f]):
            return (m[i], 2)
        else:
            conti = 0
            contf = 0
            while (contf == conti):
                if (m[i-1] == m[i]):
                    conti += 1
                elif (m[f+1] == m[f]):
                    contf += 1
                elif (conti == 0 & contf == 0):
                    contf += 1

            if (contf > conti):
                return (m[f], 1)
            else:
                return (m[i], 1)
    else:
        med = floor((i+f)/2)
        (num1, quant1) = Moda(m, i, med)
        (num2, quant2) = Moda(m, med+1, f)
        if (num1 == num2):
            return (num1, quant1+quant2)
        else:
            if (quant1 > quant2):
                return (num1, quant1)
            else:
                return (num2, quant2)


m = [4, 3, 3, 7, 9, 6, 9, 4, 5, 5, 5, 5, 2, 1]
tam = len(m)-1
mergeSort(m, 0, tam)
print(m)
print(tam)
valor = Moda(m, 0, tam)
print('A moda é ', valor[0])
