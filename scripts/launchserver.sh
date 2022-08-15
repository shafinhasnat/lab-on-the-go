#!/bin/bash

echo OPERATION $opn
echo PORT $port
echo NAME $name

if [ $opn = "ssh" ]
then
    echo ******** VM launch intiated *******
    docker run -it -d -p $port:22 --name $name shafinhasnat/sshserver
    echo ***********************************
else
    echo ******** Terminal launch intiated *******
    docker run -it -d -p $port:5000 --name $name shafinhasnat/termserver
    echo ***********************************
fi
echo "docker stop $name && docker rm $name" | at now + 1 hour