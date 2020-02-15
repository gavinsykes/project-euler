<?php
require_once '../php_functions.php';

function euler_4($n) {
    if (($n < 1) || !is_int($n)) {
        return undefined;
    }

    $result = 0
    for ($i = 1; $i <= 10**$n; $i++) {
        for ($j = 1; $j <= 10**$n; $j++) {
            $prod = $i*$j;
            if (is_palindrome($prod) && $prod > $result) {
                $result = $prod;
            }
        }
    }
    return $result;
}

$v = $_REQUEST['val'];

echo euler_4($v);
