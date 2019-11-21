<?php
function euler_2($n) {
    $result = 0;
    $i = 1;
    while (fibonacci($i) < $n) {
        $i++;
        $f = fibonacci($i);
        if (!($f & 1)) {
            $result += $f;
        }
    }
    return $result;
}
echo euler_2(4000000); // Returns 4613732
// Function to work out the fibonacci numbers. Done as an array because it is much much faster than using a recursive function.
function fibonacci($n) {
    if (!is_int($n) || $n < 1) {
        return undefined; // Didn't really need this as I'm controlling the input, but you just never know.
    }
    if ($n == 1 || $n == 2) {
        return $n;
    }
    $result = [1,2];
    for ($i = 2;$i < $n;$i++) {
        $result[$i] = $result[$i-1] + $result[$i-2];
    }
    return $result[$n-1];
}
?>
