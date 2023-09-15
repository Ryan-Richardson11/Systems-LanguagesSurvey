package main

import "fmt"

// Returns tribonacci sequence for a given input n.
func tribonacci(n int) []int {
	if n <= 0 {
		return []int{}
	} else if n == 1 {
		return []int{0}
	} else if n == 2 {
		return []int{0, 1}
	} else {
		fib_seq := []int{1, 1, 1}
		for i := 3; i < n; i++ {
			next_num := fib_seq[i-1] + fib_seq[i-2] + fib_seq[i-3]
			fib_seq = append(fib_seq, next_num)
		}
		return fib_seq
	}
}

func main() {
	fmt.Println(tribonacci(20))
}
