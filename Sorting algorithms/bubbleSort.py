def bubbleSort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor

vetorInitial = input("Digite os valores: ")
vetor = list(map(int, vetorInitial.split()))

print(f"Vetor original: {vetor}")
print(f"Vetor ordenado: {bubbleSort(vetor)}")