<?php
function is_even(int $n) {
    return !($n & 1);
}

function is_odd(int $n) {
    return $n & 1;
}

function is_pythagorean_triple(int $a,int $b,int $c) {
    $a_squared = $a**2;
    $b_squared = $b**2;
    $c_squared = $c**2;
    if ($a_squared + $b_squared == $c_squared || $a_squared + $c_squared == $b_squared || $b_squared + $c_squared == $a_squared) {
        return true;
    }
    return false;
}

function is_palindrome(string $s) {
    $str = strval($s);
    if ($str == strrev($str)) {
        return true;
    }
    return false;
}

function is_prime(int $n) {
    if ($n < 1 || !is_int($n)):
        return false;

    if(is_even(n)):
        return false;

    if($n % 3 == 0):
        return false;

    if((substr(strval($n),-1) == '5') || (substr(strval($n),-1) == '0')):
        return false;

    for ($i = 1; $i < $n/6; $i++) {
        if($n % (6 * $i - 1) == 0 || $n % (6 * $i + 1) == 0) {
            return false;
        }
    }

    return true;
}

function product_of_array(array $a) {
    $result = 1;
    foreach($a as $v) {
        $result *= $v;
    }
    unset($v);
    return $result;
}
?>
