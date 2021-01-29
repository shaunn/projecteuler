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

fn main() {
    let upper_limit = 10;
    let _test_divisors = [3,5];
    let mut _summer = 0;

    for _number in 0..upper_limit {
        for _divisor in &_test_divisors {
            if test_if_multiple(_number,*_divisor) {
                _summer = _summer + _number;
                break
            }
        }
    }
    println!("{}", _summer);
}

fn test_if_multiple(_number: i32, _divisor: i32) -> bool{
    if _number%_divisor == 0 {
        return true
    }
    return false
}