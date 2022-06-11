#!/bin/bash
   declare -a array=("192.168.0.1" "173.194.222.113" "87.250.250.242") 
   k=0
   for ((;;)); do
   curl http://${array[$k]}:80 > /dev/null
   if [[ $? != 0 ]]; then
        echo "${array[$k]} connect NO" >> error.log
        break
   elif [[ $k == 2 ]]; then
        k=$((0+0))
   else
        k=$(($k+1))
   fi
done
