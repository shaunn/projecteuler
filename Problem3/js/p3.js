// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?
//
//     The test
// const number = 13195;
// Answer is [5,7,13,29]

const number = 600851475143;

// List of discovered primes
let primes = [];

// List of discovered prime factors
let prime_factors = [];

// Define the potential primes prior to eval
let prime_candidate = 1

let dividend

console.log("Find the largest prime factor of ", number)
dividend = number
prime_factor_search(dividend)
console.log("Answer: ", prime_factors[prime_factors.length -1])
console.log("Number of prime_factors: ", prime_factors.length)
console.log("Number of discovered primes: ", primes.length)

function prime_factor_search(dividend) {
    if (primes.length === 0) {
        primes.push(prime_candidate);
    }

    prime_candidate = primes[primes.length-1] + 1;

    while (true) {

        if (prime_candidate > dividend) {
            break;
        }

        let is_prime = primes.every(evalCandidate)
        if (is_prime) {
            primes.push(prime_candidate);
            if (dividend % prime_candidate === 0) {
                    prime_factors.push(prime_candidate)
                dividend = dividend / prime_candidate
            }
        }
        prime_candidate++;
    }
}

function evalCandidate(prime) {
    // Just load 2 into the array already
    // if (prime === 1 && primes.length === 1){
    if (primes.length === 1) {
        return true
    }

    // Everything is divisible by 1, so move on to the next
    if  (prime === 1) {
        return true
    }

    if (primes.includes(prime_candidate)) {
        console.log("included " + prime_candidate)
        return true
    }

    if (prime_candidate % prime === 0) {
        dividend = dividend / prime_candidate
        // prime_factors.push(prime_candidate)
    }
    else {
        return true
    }
}