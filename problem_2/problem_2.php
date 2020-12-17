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

function fibonacci($n) {
    if (!is_int($n) || $n < 1) {
        return undefined;
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

$v = $_REQUEST['val'];

echo euler_2($v);
?>
