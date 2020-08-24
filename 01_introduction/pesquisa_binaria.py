def pesquisa_binaria(lista, item):
  # baixo e alto acompanham a parte da ;lista que você está procurando
  baixo = 0
  alto = len(lista) - 1

  # enquanto ainda não conseguiu chegar a um único elemento...
  while baixo <= alto:
    # ...verifica o elemento central
    meio = (baixo + alto) / 2
    chute = lista[meio]
    # Acha o item
    if chute == item:
      return meio
    # O chute foi muito alto.
    if chute > item:
      alto = meio - 1
    # O chute foi muito baixo.
    else:
      baixo = meio + 1
  # O item não existe
  return None

# Vamos testá-lo!
minha_list = [1, 3, 5, 7, 9]

# Lembre-se, as listas começam no 0. O próximo endereço tem índice 1
print(pesquisa_binaria(minha_list, 3)) # => 1
# "None" significa nulo em Python. Ele indica que o item não foi encontrado.
print(pesquisa_binaria(minha_list, -1)) # => None