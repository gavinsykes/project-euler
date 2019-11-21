const largestPalindromProduct = n => {
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
    s = s.toString();
    if (s.length === 1) {
        return true;
    }
}
