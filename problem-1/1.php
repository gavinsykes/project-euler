<?php
function euler_1($n) {
    $result = 0;
    $x = $n/3;
    $y = $n/5;
    for ($i = 1;$i<$x;$i++) {
        $result += 3 * $i;
    }
    for ($i = 1;$i<$y;$i++) {
        // If statement to make sure we haven't already added the number as a multiple of 3
        if (!(5*$i % 3 == 0)) {
            $result += 5 * $i;
        }
    }
    return $result;
}
echo euler_1(1000); // Returns 233168
