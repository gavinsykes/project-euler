<?php
function gen_max_prime($n) {
    if (($n < 1) or !is_int($n)) {
        return undefined;
    }

    while(!($n&1)) {
        $result = 2;
        $n >> 1;
    }

    for ($i = 3;sqrt($n) + 1,$i += 2) {
        while ($n%$i == 0) {
            $result = $i;
            $n = $n / $i;
        }
    }

    if ($n > 2) {
        $result = $n;
    }

    return $result;
}

$v = $_REQUEST['val'];

echo gen_max_prime($v);
?>
