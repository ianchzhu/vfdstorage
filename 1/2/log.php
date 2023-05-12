<?php
    $name = $_POST['name']; // Retrieve the name from the submitted form
    $ipaddress = $_SERVER['REMOTE_ADDR']; // Retrieve the IP address of the visitor
    
    // Open the log file in append mode
    $logfile = fopen("log.txt", "a");
    
    // Write the name and IP address to the log file
    fwrite($logfile, "$name,$ipaddress\n");
    
    // Close the log file
    fclose($logfile);
?>