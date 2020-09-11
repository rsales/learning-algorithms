# ================
# pseudocodigo mode ON
# ================

def procure_pela_chave(caixa_principal):
  # monte uma pilha com as caixas que serao analisadas
  pilha = main_box.crie_uma_pilha_para_busca()
  # execute enquanto a pilha nao estiver vazia
  while pilha is not vazia:
    # pegue a caixa e olhe o que tem dentro
    caixa = pilha.pegue_caixa()
    for item in caixa:
      # se voce encontrar outra caixa dentro dela...
      if item.e_uma_caixa():
        # ... adicione-a a um novo monte para verificar mais tarde
        pilha.append(item)
      # se voce encontrar uma chave terminou!
      elif item.e_uma_chave():
        print("Achei a chave!")
  # repita...