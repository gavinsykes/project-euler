<?php
define("CLI", defined("STDIN")
    || (
        empty($_SERVER["REMOTE_ADDR"])
        && !isset($_SERVER["HTTP_USER_AGENT"])
        && count($_SERVER["argv"]) > 0
    )
);
function prepare_csv_timings_file(int $problem_number): void {
    if (csv_timings_file_exists($problem_number)) {
        if (!csv_timings_file_is_empty($problem_number)) {
            if (!csv_timings_file_prepared($problem_number)) {
                return;
            } else {
                throw new Exception(sprintf("The CSV timings file for problem %s isn't prepared, but also doesn't appear to be empty. Manual intervention required.",$problem_number));
            }
        }
    }
    // Below still to be converted to Python
      with open(this_directory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '_timings.csv', 'w', newline='') as csv_file:
          writer = csv.writer(csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
          writer.writerow(['language', 'language_version', 'input', 'time', 'os', 'os_release', 'os_version', 'machine', 'processor', 'cpu_freq', 'memory', 'timestamp'])
          csv_file.close()
}
function append_data_to_csv_timings_file(int $problem_number, string $language, string $language_version, int $input, float $time, string $operating_system, string $os_release, string $os_version, string $machine, string $processor, int $cpu_freq, int $memory, float $timestamp):void {}

function full_print(string $challenge,$fun,int $arg): void {
    $file_path = explode("/",debug_backtrace()[0]["file"]);
    $problem_number = explode(".",explode("_",$file_path[count($file_path) - 1])[1])[0];
    $timing = [
        "start"  => microtime(true),
        "finish" => NULL
    ];
    if ($arg) {
        $result = $fun($arg);
    } else {
        $result = $fun();
    }
    $timing['finish'] = microtime(true);
    echo $challenge . PHP_EOL;
    echo sprintf("Start time: %s",$timing["start"]) . PHP_EOL;
    echo sprintf("Result: %s",$result) . PHP_EOL;
    echo sprintf("End time: %s",$timing["finish"]) . PHP_EOL;
    echo sprintf("This returns %s in %s seconds!",$result,$timing["finish"] - $timing["start"]) . PHP_EOL;
    try {
        $env_file = file_get_contents("env_info.json");
        $environment = json_decode($env_file);
    } catch (Exception $error) {
        throw new \Exception("\x1b[1;31m" . "Environment info JSON file not found, it should be in root and be called \"env_info.json\". Try running \"python3 get_env.py\" first." . "\x1b[0m");
    }
    $php_version = [
        "major"   => PHP_MAJOR_VERSION,
        "minor"   => PHP_MINOR_VERSION,
        "release" => PHP_RELEASE_VERSION
    ];
    $operating_system = $environment["os"];
    $os_release = $environment['os_release'];
    $os_version = $environment['os_version'];
    $machine = $environment['machine'];
    $processor = $environment['processor'];
    $cpu_freq = $environment['cpu_freq'];
    $memory = $environment['memory'];
    prepare_csv_timings_file($problem_number);
    append_data_to_csv_timings_file($problem_number,'PHP', implode(".",$php_version),$arg,$timing['finish'] - $timing['start'],$operating_system,$os_release,$os_version,$machine,$processor,$cpu_freq,$memory,$timing['start']);
}

function is_even(int $n) {
    return !($n & 1);
}

function is_odd(int $n) {
    return $n & 1;
}

function is_pythagorean_triple(int $a,int $b,int $c) {
    $a_squared = $a**2;
    $b_squared = $b**2;
    $c_squared = $c**2;
    if ($a_squared + $b_squared == $c_squared || $a_squared + $c_squared == $b_squared || $b_squared + $c_squared == $a_squared) {
        return true;
    }
    return false;
}

function is_palindrome(string $s) {
    $str = strval($s);
    if ($str == strrev($str)) {
        return true;
    }
    return false;
}

function is_prime(int $n) {
    if (
        $n < 1
        || !is_int($n)
        || is_even($n)
        || $n % 3 == 0
        || (substr($n,-1) == "5") || (substr($n,-1) == "0")
    ) {
        return false;
    }

    for ($i = 1; $i < $n/6; $i++) {
        if($n % (6 * $i - 1) == 0 || $n % (6 * $i + 1) == 0) {
            return false;
        }
    }

    return true;
}

function product_of_array(array $a) {
    $result = 1;
    foreach($a as $v) {
        $result *= $v;
    }
    unset($v);
    return $result;
}
?>
