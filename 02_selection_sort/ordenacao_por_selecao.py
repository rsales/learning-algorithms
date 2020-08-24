# Encontando o menor valor no array
def buscaMenor(arr):
  # Armazena o menor valor
  menor = arr[0]
  # Armazena o indce do menor valor
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor_indice = i
      menor = arr[i]      
  return menor_indice

# ordenacoes em um array
def ordenacaoporSelecao(arr):
  novoArr = []
  for i in range(len(arr)):
      # Encontre o menor elemento do array e adiciona ao novo array
      smallest = buscaMenor(arr)
      novoArr.append(arr.pop(smallest))
  return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))