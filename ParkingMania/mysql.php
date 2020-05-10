<?php
// connect to the database
define('DB_USER', '2020S_KEP');
define('DB_PASSWORD', '2020S_MDB');
define('DB_HOST', 'imc.kean.edu');
define('DB_NAME', '2020S_KEP');

// Make the connection:
$db = @mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) OR die('Could not connect to MySQL: ' . mysqli_connect_error() );

// Set the encoding...
mysqli_set_charset($db, 'utf8');
?>