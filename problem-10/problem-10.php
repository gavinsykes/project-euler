<?php
function euler_10($n) {
    $result = [
        'terms' => [],
        'answer' => 0
    ];
    for ($i = 1;$i < $n; $i++) {
        if (is_prime($i)) {
            $result['answer'] += $i;
            array_push($result['terms'],$i);
        }
    }
    return json_encode($result);
}

$v = $_REQUEST['val'];

echo euler_10($v);
