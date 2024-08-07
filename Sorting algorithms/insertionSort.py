def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        key = vetor[i]
        j = i - 1
        while j >= 0 and key < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = key
    return vetor

vetorInitial = input("Digite os valores: ")
vetor = list(map(int, vetorInitial.split()))

print(f"Vetor original: {vetor}")
print(f"Vetor ordenado: {insertion_sort(vetor)}")