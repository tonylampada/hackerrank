# https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true

# O movimento da rainha é limitado por obstáculos nas 8 direções da rosa dos ventos (e, w, n, s, ne, nw, se, sw)
# Esses obstaculos podem ser reais (presentes na lista de obstaculos) ou imaginarios (fora do tabuleiro)
# É facil encontrar esses obstaculos em (e, w, n, s).
# Nas diagonais é mais trabalhoso. 
# Pra isso é preciso identificar as diagonais e aí vale o notar o seguinte fato:
# 2 casas estão na mesma diagonal ascendente quando a diferença r - c é a mesma
# 2 casas estão na mesma diagonal descendente quando a soma r + c é a mesma
# Com isso a gente procura as casas que limitam o movimento ne, nw, se, sw (no codigo, só fui atrás de saber a coluna)
# Uma vez encontrados os 8 limitantes é só somar tudo.

# n = 4
# k = 0
# r_q = 4
# c_q = 4
# obstacles = []
# expect = 9

n = 100
k = 100
r_q = 48
c_q = 81
obstacles = [[54, 87],[64, 97],[42, 75],[32, 65],[42, 87],[32, 97],[54, 75],[64, 65],[48, 87],[48, 75],[54, 81],[42, 81],[45, 17],[14, 24],[35, 15],[95, 64],[63, 87],[25, 72],[71, 38],[96, 97],[16, 30],[60, 34],[31, 67],[26, 82],[20, 93],[81, 38],[51, 94],[75, 41],[79, 84],[79, 65],[76, 80],[52, 87],[81, 54],[89, 52],[20, 31],[10, 41],[32, 73],[83, 98],[87, 61],[82, 52],[80, 64],[82, 46],[49, 21],[73, 86],[37, 70],[43, 12],[94, 28],[10, 93],[52, 25],[50, 61],[52, 68],[52, 23],[60, 91],[79, 17],[93, 82],[12, 18],[75, 64],[69, 69],[94, 74],[61, 61],[46, 57],[67, 45],[96, 64],[83, 89],[58, 87],[76, 53],[79, 21],[94, 70],[16, 10],[50, 82],[92, 20],[40, 51],[49, 28],[51, 82],[35, 16],[15, 86],[78, 89],[41, 98],[70, 46],[79, 79],[24, 40],[91, 13],[59, 73],[35, 32],[40, 31],[14, 31],[71, 35],[96, 18],[27, 39],[28, 38],[41, 36],[31, 63],[52, 48],[81, 25],[49, 90],[32, 65],[25, 45],[63, 94],[89, 50],[43, 41]]
expect = 40

def queensAttack(n, k, r_q, c_q, obstacles):
    DP_q = r_q - c_q
    DN_q = r_q + c_q
    Lim_c_DP_ne = n + 1 - max(0, DP_q)
    Lim_c_DP_sw = -min(0, DP_q)
    Lim_c_DN_se = min(DN_q, n + 1)
    Lim_c_DN_nw = max(0, DN_q - (n + 1))
    Ec = min([n + 1] + [o[1] for o in obstacles if o[0] == r_q and o[1] > c_q])
    Wc = max([0] + [o[1] for o in obstacles if o[0] == r_q and o[1] < c_q])
    Nr = min([n + 1] + [o[0] for o in obstacles if o[1] == c_q and o[0] > r_q])
    Sr = max([0] + [o[0] for o in obstacles if o[1] == c_q and o[0] < r_q])
    NEc = min([Lim_c_DP_ne] + [o[1] for o in obstacles if o[0] - o[1] == DP_q and o[1] > c_q])
    SWc = max([Lim_c_DP_sw] + [o[1] for o in obstacles if o[0] - o[1] == DP_q and o[1] < c_q])
    SEc = min([Lim_c_DN_se] + [o[1] for o in obstacles if o[0] + o[1] == DN_q and o[1] > c_q])
    NWc = max([Lim_c_DN_nw] + [o[1] for o in obstacles if o[0] + o[1] == DN_q and o[1] < c_q])
    Ae = Ec - c_q - 1
    Aw = c_q - Wc - 1
    An = Nr - r_q - 1
    As = r_q - Sr - 1
    Ane = NEc - c_q - 1
    Asw = c_q - SWc - 1
    Ase = SEc - c_q - 1
    Anw = c_q - NWc - 1
    attack_ewns_neswsenw = [Ae, Aw, An, As, Ane, Asw, Ase, Anw]
    print(attack_ewns_neswsenw)
    return sum(attack_ewns_neswsenw)

actual = queensAttack(n, k, r_q, c_q, obstacles)
print(actual == expect)
