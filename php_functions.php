<?php
function is_pythagorean_triple(int $a,int $b,int $c) {
    if ($a**2+$b**2==$c**2 || $a**2+$c**2==$b**2 || $b**2+$c**2==$a**2) {
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
        return undefined;

    if(!($n & 1)):
        return false;

    if($n % 3 == 0):
        return false;

    if(substr(strval($n),-1) == '5') || (substr(strval($n),-1) == '0')):
        return false;

    for ($i = 1; $i < $n/6; $i++) {
        if($n % (6 * $i - 1) == 0 || $n % (6 * $i + 1) == 0) {
            return false;
        }
    }

    return true;
}

function product(array $a) {
    $result = 1;
    foreach($a as $v) {
        $result *= $v;
    }
    unset($v);
    return $result;
}
?>
