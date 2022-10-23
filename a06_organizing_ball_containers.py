# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true

# Repare que a quantidade de bolas num balde nunca muda. Porque a cada operação, sai 1 bola, entra 1 bola.
# Então se tem 40 bolas azuis espalhadas em n baldes. Se não tiver pelo menos um balde com 40 bolas, fodeu pro azul.
# E se tiver, vai dar bom. É só eu jogar azul lá (trocando por qualquer coisa que não for azul)
# Uma vez resolvido o azul, parto pra próxima cor.
# Então, se as quantidade de bolas nos baldes forem as mesmas das quantidades de bolas de cada cor, dá bom 

containers = [
    [[1, 1], [1, 1]],
    [[0, 2], [1, 1]]
]
expect = ['Possible', 'Impossible']

def organizingContainers(container):
    n = len(container)
    byBucket = {i: sum(container[i]) for i in range(n)}
    byColor = {j: sum([container[i][j] for i in range(n)]) for j in range(n)}
    return 'Possible' if sorted(byBucket.values()) == sorted(byColor.values()) else 'Impossible'

actual = [organizingContainers(c) for c in containers]
print(actual == expect)
