<?php
function euler_1($n) {
    $result = [
        'terms' => [],
        'answer' => 0
    ];
    $x = $n/3;
    $y = $n/5;
    for ($i = 1;$i<$x;$i++) {
        $result['answer'] += 3 * $i;
        array_push($result['terms'],3 * $i);
    }
    for ($i = 1;$i<$y;$i++) {
        if (!(5*$i % 3 == 0)) {
            $result['answer'] += 5 * $i;
            array_push($result['terms'],5 * $i);
        }
    }
    sort($result['terms']);
    if (count($result['terms']) == 0) {
        $result['answer'] = 0;
    }
    return json_encode($result);
}

$v = $_REQUEST['val'];

echo euler_1($v);
?>
