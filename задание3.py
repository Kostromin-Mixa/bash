#!/bin/bash
   func(){
   h=0
   while [ $h -lt 5 ]; do
   curl http://$1:80 > /dev/null
   if (( $? != 0 )); then
   echo "$1 connect NO" >> status.log
   break
   elif [[ $h == 3 ]]; then
   echo "$1 connect OK" >> status.log
   fi
   h=$(($h+1))
   done
   }
   declare -a array=("192.168.0.1" "173.194.222.113" "87.250.250.242")
   j=0
   while [ $j -lt 3 ]; do
   func ${array[$j]}
   j=$(($j+1))
done
