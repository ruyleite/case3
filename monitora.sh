#!/bin/bash    
./$1 &
P1=$!
psrecord $P1 --interval 0.5 --duration 600 --plot plot_$1.png &
P1=$!
wait $P1 
echo 'Done'

