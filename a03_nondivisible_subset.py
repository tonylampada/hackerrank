# https://www.hackerrank.com/challenges/non-divisible-subset/problem?h_r=profile

# s = [1, 7, 2, 4]
# k = 3
# expect = 3

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 4
expect = 5

# Ideia:
# - os numeros nao importam, só os numeros modulo k
# por exemplo [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] vira [1,2,3,0,1,2,3,0,1,2]
# ou seja, 4 é "um 0" (modulo 4), 10 é "um 2" (modulo 4)
# pra montar um subset, vc não pode: 
# - ter 2 elementos 0 (pq 0 + 0 = 0)  
# - ter 2 elementos 2 (pq 2 + 2 = 0)
# - ter 2 elementos com modulo complementar (1 e 3)
# Então contando os modulos de s vc pode montar o dicionario {0:2, 1:3, 2:2, 3:2}
# Esquece o conjunto S. O input que importa é esse dicionario aí pq olhando pra ele a gente pode montar o maior conjunto viável:
# 0: 2. Tem 2 zeros. Podia ter 300, mas eu só posso pegar 1 (+1)
# 2: 2. Idem (+1)
# 1:3, 3: 2. 1 e 3 são complementares. Eu só posso pegar de um ou de outro. Vou pegar do 1 que tem mais. (+3)
# Resultado = 5

def nonDivisibleSubset(k, s):
    if k == 1:
        return 1
    d = {r:0 for r in range(k)}
    for e in s:
        key = e % k
        d[key] = d[key] + 1
    s = 0
    for r in range(k//2 + 1):
        comp = 0 if r == 0 else k - r
        if r in {0, k/2}:
            s += min(1, d[r])
        else:
            s += max(d[r], d[comp])
    print(d, s)
    return s

actual = nonDivisibleSubset(k, s)
print(actual == expect)