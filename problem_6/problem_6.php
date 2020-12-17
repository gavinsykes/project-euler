<?php
function euler_6($n) {
    if ($n < 1 || !is_int($n)) {
        return undefined;
    }

    $result = 0;
    $sumsquares = 0;
    $sum = 0;
    $squaresum = 0;
    for ($i = 1; $i <= $n; $i++) {
        $sumsquares += $i**2;
    }
    for ($i = 1; $i <= $n; $i++) {
        $sum += $i;
    }
    $squaresum = $sum**2;
    $result = $squaresum - $sumsquares;
    return $result;
}

$v = $_REQUEST['val'];

echo euler_6($v);
