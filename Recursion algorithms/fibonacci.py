def fibonacci(n):
    if n == 0:
        print("O número precisa ser um inteiro maior que zero")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

n = int(input("Digite quantos elementos a sequencia deve conter: "))
print(f"{fibonacci(n)}")