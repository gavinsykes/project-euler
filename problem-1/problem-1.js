const euler_1 = n => {
    let result = 0,
    x = n/3,
    y = n/5

    for (let i = 1; i < x; i++) {
        result += i*3;
    }

    for (let i = 1; i < x; i++) {
        if (5*i % 3 != 0) {
            result += i*5;
        }
    }

    return result;
};
