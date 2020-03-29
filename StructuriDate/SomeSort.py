def creare_vector(size, max):
    from random import randint
    return [randint (0, max) for _ in range(size)]

def bubble(v):
    if len(v) >= 3000:
        print("Nu se poate efectua Bubble Sort pentru atat de multe numere")
    else:
        for i in range(0,len(v)):
            for j in range (0, len(v)-1):
                if v[j] > v[j+1]:
                    aux = v[j]
                    v[j] = v[j+1]
                    v[j+1] = aux
        return v

def count(v):
    if v != []:
        if max(v) >= 10**6:
            print("Nu se poate efectua Count Sort pentru numere de dimensiuni atat de mari")
        else:
            a = [0]*(max(v)+1)
            v2 = []
            for i in v:
                a[i] += 1
            for i in range(max(v)+1):
                    for j in range(1, a[i]+1):
                        v2 = v2 + [i]
            return v2
    else: return v

def radix(A):
    max1 = max(A)
    nr = 0
    while max1 != 0:
        nr = nr + 1
        max1 = max1 // 10
    for p in (10 ** k for k in range(0, nr)):
        v = [0] * 10
        B = [0] * len(A)
        for i in range(len(A)):
            v[(A[i] // p) % 10] += 1
        for i in range(1, 10):
            v[i] = v[i] + v[i - 1]
        for i in range(len(A) - 1, -1, -1):
            v[(A[i] // p) % 10] -= 1
            B[v[(A[i] // p) % 10]] = A[i]
        A = B
    return A

def merge(a,b):
    c = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c

def merge_sort(a):
    if len(a) <= 1:
        return a
    left,right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
    return merge(left,right)

def quick_sort(a):
    from random import randint
    if len(a) <= 1:
        return a
    lower, equal, greater = [], [], []
    pivot = a[randint(0, len(a)-1)]
    for x in a:
        if x < pivot:
            lower.append(x)
        elif x == pivot:
            equal.append(x)
        else: greater.append(x)
    return quick_sort(lower) + equal + quick_sort(greater)

def testare(v):
    if (v == None):
        return "NU"
    ok = 1
    for i in range(0,len(v)-1):
        if v[i] > v[i+1]:
            ok = 0
    if ok == 0:
        return "NU"
    else: return "DA"

q = open("TESTARI.txt", 'r')
n = int(q.readline())
from time import time
l = q.readlines()
for x in l:
    x = x.split()
    x = [int(j) for j in x]
    v = creare_vector(x[0],x[1])
    print("N = " + str(x[0]) + ", Max = " + str(x[1]))
    cv = list()
    for index in range(len(v)):
        cv.append(v[index])
    t0 = time()
    cv = bubble(cv)
    t1 = time()
    calificativ = testare(cv)
    print("BubbleSort: ", str(t1-t0), calificativ)

    cv = list()
    for index in range(len(v)):
        cv.append(v[index])
    t0 = time()
    cv = count(cv)
    t1 = time()
    calificativ = testare(cv)
    print("CountSort: ", str(t1-t0), calificativ)

    cv = list()
    for index in range(len(v)):
        cv.append(v[index])
    t0 = time()
    cv = radix(cv)
    t1 = time()
    calificativ = testare(cv)
    print("RadixSort: ", str(t1-t0), calificativ)

    cv = list()
    for index in range(len(v)):
        cv.append(v[index])
    t0 = time()
    cv = merge_sort(cv)
    t1 = time()
    calificativ = testare(cv)
    print("MergeSort: ", str(t1-t0), calificativ)

    cv = list()
    for index in range(len(v)):
        cv.append(v[index])
    t0 = time()
    cv = quick_sort(cv)
    t1 = time()
    calificativ = testare(cv)
    print("QuickSort: ", str(t1-t0), calificativ)