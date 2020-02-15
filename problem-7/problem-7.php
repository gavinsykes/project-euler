<?php
function euler_7($n) {
    if ($n < 1 || !is_int($n)) {
        return undefined;
    }

    $r = 0;
    $count = 1;
    while ($count <= $n) {
        if (is_prime(2*$r+1)) {
            $count++;
        }
        $r++;
    }
    return 2 * $r + 1;
}

$v = $_REQUEST['val'];

echo euler_7($v);
