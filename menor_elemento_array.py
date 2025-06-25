def buscaMenor(arr):
    menor = arr[0]
    menor_index = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_index = i
    print(menor_index)
    return menor_index
