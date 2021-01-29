// divisors of 3 and 5
//
// Problem 1
// If we list all the natural numbers below 10 that are divisors of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these divisors is 23.
//
// Find the sum of all the divisors of 3 or 5 below 1000.
//
// Strategies
//
// 1. `remainder = dividend - divisor * quotient` and `remainder=0`
// 2. Using the built-in modulo function
// 3. Using the built-in remainder function
//
// Packages! tbd...
//
// Constants and variables!
//     Set the upper limit
var upperLimit = 1000;
// var upperLimit = 10;

// Set the list of divisors to test against
var divisors = [3, 5];

// Define the 'summer' containing the running of sums
var summer = 0;


// Functions!
function test_if_multiple(testNumber, testDivisors) {
    return test_zero_using_modulo_function(testNumber, testDivisors)
}

function test_zero_using_modulo_function(testNumber, testDivisors) {
    var numDivisors = testDivisors.length

    for (var i = 0; i < numDivisors; i++) {
        var test = testNumber%testDivisors[i]
        if (test == 0) {
            return true;
        }
    }
    // None of the divisors in the testDivisors array satisfy the test
    return false;
}

var numDivisors = upperLimit.length
for (var i = 0; i < upperLimit; i++) {
    if (test_if_multiple(i, divisors)) {
        summer = summer + i
    }
}
console.log(summer)

// if (i%%3 == 0 | i%%5 == 0)
