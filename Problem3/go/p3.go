//The prime factors of 13195 are 5, 7, 13 and 29.
//
//What is the largest prime factor of the number 600851475143 ?

package main

import (
	"fmt"
)

//The test
//const number int = 13195
//Answer is [5,7,13,29]

//The real deal
const number int = 600851475143

//Starting prime
var primeCandidate int = 1

//List of discovered primes
var primes []int

//List of discovered prime factors
var primeFactors []int

func main() {
	fmt.Println("Find the largest prime factor of: ", number)
	primeFactorSearch(number)
	fmt.Println("Answer: ", primeFactors[len(primeFactors)-1])
	fmt.Println("Number of prime_factors: ", len(primeFactors))
	fmt.Println("Discovered primes: ", len(primes))
}

func primeFactorSearch(dividend int) {

	var newPrime int

	// Initial load of primes array
	if len(primes) == 0 {
		primes = append(primes,1)
	}

	for {
		knownPrimeFound := Find(primes, primeCandidate)

		if knownPrimeFound {
			primeCandidate = primes[len(primes)-1] + 1
		}

		if primeCandidate > dividend {
			return
		}

		PRIMELOOP:
		for _, prime := range primes {
			if prime == 1 {
				continue
			}

			if primeCandidate % prime == 0 && prime != 1{
				primeCandidate++
				goto PRIMELOOP
			}
		}

		if !knownPrimeFound {
			primes = append(primes, primeCandidate)
			if dividend%primes[len(primes)-1] == 0 {
				newPrime = primes[len(primes)-1]
				primeFactors = append(primeFactors, newPrime)
				dividend = dividend / newPrime
				primeCandidate++
			}
		}
	}
}

func Find(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}
