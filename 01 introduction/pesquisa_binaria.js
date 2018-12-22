// Method development test binary search
const pesquisaBinaria = (lista, item) => {
  let baixo = 0;
  let alto = lista.length - 1;

  while (baixo <= alto) {
    const meio = Math.floor((baixo + alto) / 2);
    const chute = lista[meio];

    if (chute == item) {
      return meio
    }
    else if (chute > item) {
      alto = meio - 1
    }
    else {
      baixo = meio + 1
    }
  }
  return null
};

const minha_lista = [1, 3, 5, 7, 9];

console.log(pesquisaBinaria(minha_lista, 3)); // 1
console.log(pesquisaBinaria(minha_lista, -1)); // nil