package main

import (
	"fmt"
	"strconv"
)

func addDigits(num int) int {

	numstr := strconv.Itoa(num)

	if len(numstr) == 1 {
		return num
	} else {
		var running_sum int

		for _, val := range numstr {
			digit, _ := strconv.Atoi(string(val))
			running_sum += digit
		}
		return addDigits(running_sum)
	}

}

func main() {
	a := 12345
	b := addDigits(a)

	fmt.Println(b)
}
