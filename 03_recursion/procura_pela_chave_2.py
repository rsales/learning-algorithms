# ================
# pseudocodigo mode ON
# ================

def procure_pela_chave(caixa):
  # olhe dentro da caixa
  for item in caixa:
    # se encontrar outra caixa...
    if item.e_uma_caixa():
      # ... volte ao passo 1
      procure_pela_chave(item) # recursao!
    # se encontrar a chave, terminou
    elif item.e_uma_chave():
      print("Achei a chave!")    
