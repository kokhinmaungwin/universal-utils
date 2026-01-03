<?php
// utils.php

function capitalize(string $text): string {
    if (empty($text)) return '';
    return ucfirst($text);
}

function debounce(callable $func, int $wait = 300) {
    // PHP doesn't handle async easily, so debounce is more frontend concern
    // This is just a placeholder
    return $func;
}

function throttle(callable $func, int $limit = 300) {
    // Similarly, no straightforward throttle in PHP
    return $func;
}

function copy_to_clipboard(string $text) {
    // No direct clipboard in PHP (server side)
    // This function can echo JS to copy clipboard on frontend
    echo "<script>navigator.clipboard.writeText(" . json_encode($text) . ");</script>";
}

function format_date(DateTime $date): string {
    return $date->format('Y-m-d');
}
?>
