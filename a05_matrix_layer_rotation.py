# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=true

# Aff que problema top. Divertidissimo isso.
# A ideia é simples mas tem um pulo do gato que é "desenrolar" cada camada da matrix transformando ela numa lista.
# Aí rotaciona a lista
# E "enrola" ela de novo na nova matriz.
# Poderia até usar a matriz original se vc tiver com dó de gastar memoria :P

matrix = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
]
r = 1
expect = [
    [2, 3, 4, 8],
    [1, 7, 11, 12],
    [5, 6, 10, 16],
    [9, 13, 14, 15],
]

# matrix = [
#     [1,   2,  3,  4],
#     [7,   8,  9, 10],
#     [13, 14, 15, 16],
#     [19, 20, 21, 22],
#     [25, 26, 27, 28],
# ]
# r = 7
# expect = [
#     [28, 27, 26, 25],
#     [22,  9, 15, 19],
#     [16,  8, 21, 13],
#     [10, 14, 20,  7],
#     [4,   3,  2,  1],
# ]


def matrixRotation(matrix, r):
    M, N = len(matrix), len(matrix[0])
    K = min(M, N) // 2
    rmatrix = [[None] * N for i in range(M)]
    for d in range(K):
        rotateLayer(matrix, rmatrix, d, r)
    return rmatrix


def rotateLayer(matrix, rmatrix, d, r):
    l = desenrola(matrix, d)
    rr = r % len(l)
    l = l[rr:] + l[0:rr]
    enrola(rmatrix, l, d)


def desenrola(matrix, d):
    M, N = len(matrix), len(matrix[0])
    l = matrix[d][d:N-d]
    for i in range(d+1, M-d-1):
        l.append(matrix[i][N-d-1])
    l += matrix[M-d-1][d:N-d][::-1]
    for i in range(d+1, M-d-1)[::-1]:
        l.append(matrix[i][d])
    return l


def enrola(rmatrix, l, d):
    M, N = len(rmatrix), len(rmatrix[0])
    lA = l[0:len(l)//2]
    lB = l[len(l)//2:]
    l1 = lA[0:N-2*d]
    l2 = lA[N-2*d:]
    l3 = lB[0:N-2*d][::-1]
    l4 = lB[N-2*d:][::-1]
    line1 = rmatrix[d]
    line2 = rmatrix[M-d-1]
    line1[d:N-d] = l1
    for i in range(len(l2)):
        rmatrix[i+d+1][N-d-1] = l2[i]
    line2[d:N-d] = l3
    for i in range(len(l4)):
        rmatrix[i+d+1][d] = l4[i]


actual = matrixRotation(matrix, r)
print(actual)
print(actual == expect)