def subsets(conjunto):
    def subsetsAux(atual, indice):
        if indice == len(conjunto):
            subconjuntos.append(atual[:])
            return

        subsetsAux(atual, indice + 1)

        atual.append(conjunto[indice])
        subsetsAux(atual, indice + 1)
        atual.pop()

    subconjuntos = []
    subsetsAux([], 0)
    return subconjuntos

conjunto = input("Digite os valores do conjunto: ")
conjunto = conjunto.split()
resultados = subsets(conjunto)

print("Subconjuntos existentes: ")
for subconjunto in resultados:
    print(subconjunto, end=' ')