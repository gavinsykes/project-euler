const euler6 = num => {
    let n = +num;
    let result = 0,
        sumsquares = 0,
        sum = 0,
        squaresum = 0;

    if (n < 1 || !Number.isInteger(n)) {
        return undefined;
    }

    for(let i = 1; i <= n; i++) {
        sumsquares += Math.pow(i,2);
    }

    for(let i = 1; i <= n; i++) {
        sum += i;
    }
    squaresum = Math.pow(sum,2);

    result = Math.abs(squaresum - sumsquares);

    return result
}
