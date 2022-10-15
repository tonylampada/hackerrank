# https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
# A B C
# D E F
# G H I      
#             13
#           /
# 4   8   2   - 14
# 4   5   7   - 16
# 6   1   6   - 13
# |   |   |  \
# 14  14  15   15

# o quadrado magico tem poucas configurações viaveis porque:
# - o 5 tem que ficar no meio
# - o 1 nao pode ficar no canto (senao eu precisaria de 2 pares somando 14, mas só tem 1 par = 6,8)
# - com o 1 numa posicao de lado, 6 e 8 ficam nas quinas, aí é só escolher e terminar.
# 4 possibilidades pro 1 x 2 possibilidades pro 6 = 8 soluções:

# olha a dança do 1,6:
# 6 1 x    x 1 6    x x 6    x x x    x x x    x x x    x x x    6 x x
# x 5 x    x 5 x    x 5 1    x 5 1    x 5 x    x 5 x    1 5 x    1 5 x
# x x x    x x x    x x x    x x 6    x 1 6    6 1 x    6 x x    x x x

# que completando fica
# 6 1 8    8 1 6    2 7 6    4 3 8    4 9 2    2 9 4    8 3 4    6 7 2
# 7 5 3    3 5 7    9 5 1    9 5 1    3 5 7    7 5 3    1 5 9    1 5 9
# 2 9 4    4 9 2    4 3 8    2 7 6    8 1 6    6 1 8    6 7 2    8 3 4

SOLUTIONS = [
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
]

s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]

a,b,c,d,e,f,g,h,i = [s[i][j] for i in range(3) for j in range(3)]
INPUT = [a,b,c,d,e,f,g,h,i]

print(min([sum([abs(INPUT[k] - s[k]) for k in range(9)]) for s in SOLUTIONS]))

# 1 semana pensando, resolvido em "1 linha". Elegancia que chega a ser sensual. 