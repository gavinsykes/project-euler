const largestPalindromeProduct = num => {
    let n = +num;
    let result = 0;
    if (n < 1 || !Number.isInteger(n)) {
        return undefined;
    }

    for (let i = 1; i < 10**n;i++) {
        for (let j = 1; j < 10**n;j++) {
            if (isPalindrome(i*j) && i*j > result) {
                result = i*j;
            }
        }
    }
    return result;
}
const isPalindrome = s => !s.toString().toLowerCase().split('').filter(i => /\S/.test(i)).some((c,i,a) => c == a[a.length - 1 - i]);
