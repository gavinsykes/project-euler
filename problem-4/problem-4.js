const largestPalindromeProduct = n => {
    let result = 0;
    if (n < 1 || Number.isInteger(n)) {
        return undefined;
    }

    for (let i = 1; i < 10**n,i++) {
        for (let j = 1; j < 10**n,j++) {
            if (is_palindrome(i*j) && i*j > result) {
                result = i*j;
            }
        }
    }
}
const isPalindrome = s => {
    if (s.length === 1) {
        return true;
    }
    return !s.toString().split('').filter(i => /\S/.test(i)).map((c,i,a) => c == a[a.length - 1 - i] ? true : false).some(i => i === false);
}
