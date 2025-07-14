def buscaMenor(arr):
    menor = arr[0]
    menor_index = 0

    for i in range(len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_index = i
    print("Index: ", menor_index)
    return menor_index

def ordenacaoporSelecao(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr)
        # remove o menor item do array e o acrescenta (append) a um novo array
        novoArr.append(arr.pop(menor))
        #              ↑____________↑
        #              Executado PRIMEIRO
    return novoArr

print( "\nNew array: ", ordenacaoporSelecao([5, 3, 6, 2, 10]))