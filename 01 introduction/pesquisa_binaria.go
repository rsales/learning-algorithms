// Method development test binary search
package main

import "fmt"

func pesquisaBinaria(lista []int, item int) bool {
	baixo := 0
	alto := len(lista) - 1

	for baixo <= alto {
		meio := (baixo + alto) / 2

		if lista[meio] == item {
			return true
		}
		if lista[meio] > item {
			alto = meio - 1
		} else {
			baixo = meio + 1
		}
	}
	return false
}

func main() {
	fmt.Println(pesquisaBinaria([]int{1, 2, 3, 4, 5}, 1))  // true
	fmt.Println(pesquisaBinaria([]int{1, 2, 3, 4, 5}, -1)) //false
}
