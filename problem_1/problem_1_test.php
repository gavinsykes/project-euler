<?php
require_once("problem_1.php");

$expected_answer_file_contents = file_get_contents(__DIR__ . "/problem_1_expected_answers.json");
$expected_answers = json_decode($expected_answer_file_contents, true);

print_r($expected_answers);
$successful_tests = 0;
$failed_tests = [];

foreach ($expected_answers as $expected_answer) {
    echo "Input of $expected_answer[input] should yield $expected_answer[expected_answer]" . PHP_EOL;
    $success = false;
    $format_character = "\e[1;31m";
    $closing_format_character = "\e[0m";
    $answer = euler_1($expected_answer['input']);
    if ($answer == $expected_answer['expected_answer']) {
        $successful_tests++;
        $success = true;
        $format_character = "\e[1;32m";
    } else {
        array_push($failed_tests,[
            "input" => $expected_answer['input'],
            "expected_answer" => $expected_answer['expected_answer'],
            "actual_answer" => $answer
        ]);
    }
    echo $format_character . "Input of $expected_answer[input] yields $answer" . $closing_format_character . PHP_EOL;
}

$total_tests = $successful_tests + count($failed_tests);
echo "\e[1m" . "Total tests: $total_tests" . "\e[0m" . PHP_EOL;
echo "\e[1;32m" . "Successful tests: $successful_tests (" . $successful_tests * 100 / $total_tests . "%)" . "\e[0m" . PHP_EOL;
if (count($failed_tests) > 0) {
    echo "\e[1;31m" . "Failed tests: " . count($failed_tests) . "(" . count($failed_tests) * 100 / $total_tests . "%)" . "\033[0m" . PHP_EOL;
    foreach ($failed_tests as $test) {
        echo "\e[1;31m" . "Input of $test[input] should have yielded $test[expected_answer] but yields $test[actual_answer]" . "\033[0m" . PHP_EOL;
    }
}
?>