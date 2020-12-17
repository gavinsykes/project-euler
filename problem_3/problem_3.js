const genMaxPrime = n => {
    let result;
    if (n < 1 || !Number.isInteger(n)) {
        return undefined;
    }

    while (!(n&1)) {
        result = 2;
        n = n >> 1;
    }

    for (let i = 3; i < Math.sqrt(n);i += 2) {
        while (n % i == 0) {
            result = i;
            n = n / i;
        }
    }

    if (n > 2) {
        result = n;
    }

    return result;
};

genMaxPrime(2) =>
while(!(2&1)) = while(true)
result = 2
2 >> 1
