def sufijosOrdenados(S):
    n = len(S)
    ListaSufijos = []

    for i in range(n):
        sufijo = S[i:n]
        ListaSufijos.append(sufijo)
    return sorted(ListaSufijos)

for sufijo in sufijosOrdenados("banana"):
    print(sufijo)


