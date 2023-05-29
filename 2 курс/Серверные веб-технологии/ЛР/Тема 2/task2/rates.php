<?php
$w = 600;
$h = 400;
$ctx = imagecreate($w, $h);
imagecolorallocate($ctx, 255, 255, 255);
$rates = json_decode(file_get_contents('https://kodaktor.ru/j/rates'));
$names = array_map(function($x) { return $x -> name; }, $rates);
$sizes = array_map(function($x) { return $x -> sell; }, $rates);
$sizes = array_map(function($x) { global $sizes; return $x / max($sizes); }, $sizes);
$color = imagecolorallocate($ctx, 0, 32, 64);
$width = $w / count($sizes);
$text_color = imagecolorallocate($ctx, 0, 255, 32);
array_walk($rates, function ($x, $i) use ($ctx, $w, $h, $width, $color, $sizes, $names, $text_color) {
    imageFilledRectangle($ctx, $i*$width, $h, $i*$width+$width-5, $h-$sizes[$i]*$h, $color);
    list($left,, $right) = imageftbbox(10, 0, './Roboto-Regular.ttf', $names[$i]);
    $text_width = $right - $left;
    imageTtfText($ctx, 10, 0, $i*$width+$width / 2 - $text_width / 2, $h - 10, $text_color, './Roboto-Regular.ttf', $names[$i]);
    $i += 1;
});
header('Content-Type: image/png');
imagepng($ctx);
?>