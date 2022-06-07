#!/bin/bash

# Declare an array of string with type
declare -a StringArray=("oom-killer*" "Bug:*" "Killed process*" "Kernal panic*" "Unable to handle*" "FAT-fs*" "Out of Memory*")
# Iterate the string array using for loop
for val in "${StringArray[@]}"; do

   grep "$val" /var/log/syslog && echo "$val";

done