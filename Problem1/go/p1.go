package main

//divisors of 3 and 5
//
//Problem 1
//If we list all the natural numbers below 10 that are divisors of 3 or 5, we get 3, 5, 6 and 9.
//The sum of these divisors is 23.
//
//Find the sum of all the divisors of 3 or 5 below 1000.
//
//Strategies
//
//1. `remainder = dividend - divisor * quotient` and `remainder=0`
//2. Using the built-in modulo function
//3. Using the built-in remainder function
//
//Packages!
import (
	"fmt"
)

//Constants and variables!
var upperLimit int = 10
var summer int = 0
var testDivisors = []int{3,5}

func test_zero_using_modulo_function(test_number, test_divisor int) bool {
	var modulus int  = test_number%test_divisor
	if modulus == 0 {
		return true
	}
	return false
}

func main() {
	for i := 0; i < upperLimit; i++ {
		for _, testDivisor := range testDivisors {
			if test_zero_using_modulo_function(i, testDivisor){
				summer = summer + i
				// Since one of the divisors match for the number,
				//   break out to avoid additional summation of
				//  the number.
				break
			}
		}
	}
	fmt.Println("sum: ", summer)
}
