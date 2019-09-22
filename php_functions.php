<?php
function is_pythagorean_triple($a,$b,$c) {
    if ($a**2+$b**2==$c**2 || $a**2+$c**2==$b**2 || $b**2+$c**2==$a**2) {
        return true;
    }
    return false;
}
?>
