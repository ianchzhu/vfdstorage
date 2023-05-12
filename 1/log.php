<?php
    $name = $_POST['name']; // Retrieve the name from the submitted form
    $ipaddress = $_POST['ip']; // Retrieve the IP address from the AJAX request
    
    // Open the log file in append mode
    $logfile = fopen("log.txt", "a");
    