package main

import "fmt"

//Constants and variables!
var termLimit int = 13
var summer int = 0
//var term int = 0
//var term_1 int = 1
//var term_2 int = 0

func main() {
	var term int = 0
	var term_1 int = 1
	var term_2 int = 0
	for term < termLimit {
		fmt.Println("term: ", term)
		fmt.Println("term_1: ", term_1)
		fmt.Println("term_2: ", term_2)

		term := term_1 + term_2
		fmt.Println("term: ", term)

		if term % 2 == 0 {
			summer = summer + term
		}
		if term == 2 {
			break
		}
	}
	fmt.Println("sum: ", summer)
}