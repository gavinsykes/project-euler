import { fullPrint } from '../js_functions.cjs';

export const euler_1 = n => {
    let result = 0,
    x = n/3,
    y = n/5

    for (let i = 1; i < x; i++) {
        result += i*3;
    }

    for (let i = 1; i < y; i++) {
        if (5*i % 3 != 0) {
            result += i*5;
        }
    }

    return result;
};

if (typeof require !== 'undefined' && require.main === module) {
    fullPrint("Challenge",euler_1,1000);
}