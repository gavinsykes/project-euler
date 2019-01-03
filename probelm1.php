<?php
/* 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

function euler_1($n) {
    $result = 0;
    $x = $n/3;
    $y = $n/5;
    for ($i = 1;$i<$x;$i++) {
        $result += 3 * $i;
    }
    for ($i = 1;$i<$y;$i++) {
        // If statement to make sure we haven't already added the number as a multiple of 3
        if (!($i % 3 == 0)) {
            $result += 5 * $i;
        }
    }
    return $result;
}

echo euler_1(1000); // returns 232169
?>
