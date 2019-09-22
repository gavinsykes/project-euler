<?php
require_once '../php_functions.php';

function euler_9($n) {
    $a = $b = $c = 1;
    for ($a = 1;$a <= $n-2;$a++) {
        for ($b = 1; $b <= $n-$a-1;$b++) {
            $c = $n - $a - $b;
            if (is_pythagorean_triple($a,$b,$c)) {
                return $a . ', ' . $b . ' and ' . $c . ' make ' . $a*$b*$c . '.';
            }
        }
    }
}

$v = $_REQUEST['val'];

echo euler_9($v);
