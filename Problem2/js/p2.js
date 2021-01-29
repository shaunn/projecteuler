const term_limit = 4000000;

let summer = 0;
let term = 0;
let term_1 = 1;
let term_2 = 0;

while (term < term_limit){
    term = term_1 + term_2;

    if (term % 2 == 0){
        summer = summer + term
    }
}

console.log(summer)
