# Method development test binary search
def pesquisa_binaria(lista, item)
  baixo = 0
  alto = lista.lenght - 1

  while baixo <= alto
    meio = baixo + alto / 2
    chute = lista[meio]

    if chute == item
      return meio
    elsif chute > item
      alto = meio - 1
    else
      baixo = meio + 1
    end
  end

  return nil
end

minha_lista = [1, 3, 5, 7, 9]

puts pesquisa_binaria(minha_lista, 3) # => 1
# We need to use .inspect here because just printing nil
# would output an empty string
puts pesquisa_binaria(minha_lista, -1).inspect # => nil