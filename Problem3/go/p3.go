//The prime factors of 13195 are 5, 7, 13 and 29.
//
//What is the largest prime factor of the number 600851475143 ?

package main

import (
	"fmt"
)

//The test
const number int = 13195
//Answer is [5,7,13,29]



//The real deal
//const number int = 600851475143

//Starting prime
//var prime_candidate int = 1

//List of discovered primes
var primes []int

//List of discovered prime factors
var primeFactors []int

func main() {
	fmt.Println("Find the largest prime factor of: ", number)
	primeFactorSearch(number)
	fmt.Println("Answer: ", primeFactors[len(primeFactors)-1])
	fmt.Println("prime_factors: ", primeFactors)
	fmt.Println("Number of prime_factors: ", len(primeFactors))
	fmt.Println("Discovered primes: ", len(primes))
}

func primeFactorSearch(dividend int) {
	fmt.Println("Enter primeFactorSearch")
	fmt.Println("dividend: ", dividend)

	var newPrime int
	// Initial load of primes array
	if len(primes) == 0 {
		primes = append(primes,1)
	}

	fmt.Println("primes: ", primes)

	primeCandidate := primes[len(primes)-1]
	fmt.Println("here: ", primes)

	primeFound := Find(primes, primeCandidate)
	if primeFound {
		primeCandidate = primes[len(primes)-1] + 1
		fmt.Println("primeCandidate: ", primeCandidate)
	}

	for {
		if primeCandidate > dividend {
			return
		}
		fmt.Println("primes ", primes)


		for _, prime := range primes {
			if prime == 1 {
				fmt.Println("skip 1: ")
				continue
			}
			fmt.Println("primeCandidate ", primeCandidate)
			fmt.Println("prime: ", prime)
			fmt.Println("rimeCandidate % prime: ", primeCandidate % prime)

			if primeCandidate % prime == 0 {
				fmt.Println("primeCandidate % prime: ", primeCandidate % prime)
				fmt.Println("primeCandidate2: ", primeCandidate)
				primeCandidate++
				fmt.Println("primeCandidate3: ", primeCandidate)
				break
			}
		}

		fmt.Println("primeFound: ", primeFound)

		// This is where the lack of for..else is jacking me up
		if !primeFound {

			primes = append(primes, primeCandidate)
			fmt.Println("primes: ", primes)

			if dividend%primes[len(primes)-1] == 0 {

				newPrime = primes[len(primes)-1]
				fmt.Println("newPrime: ", newPrime)

				primeFactors = append(primes, newPrime)
				dividend = dividend / newPrime
				primeCandidate++
			}
		}
	}

}

func Find(s []int, e int) bool {
	fmt.Println("slice: ", s)
	fmt.Println("e: ", e)

	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

//        for _prime in primes:
//            if _prime == 1:
//                continue
//            if _prime_candidate % _prime == 0:
//                _prime_candidate += 1
//                break
//        else:
//            primes.append(_prime_candidate)
//            if _dividend % primes[-1] == 0:
//                # Add this new prime to the prime_factors array
//                prime_factors.append(primes[-1])
//                # Generate a new dividend to process against
//                _dividend = _dividend / primes[-1]
//                _prime_candidate += 1