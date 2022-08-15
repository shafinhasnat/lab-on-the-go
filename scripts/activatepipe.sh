#!/bin/sh

while true; do eval "$(cat /home/ubuntu/lab/mypipe.pipe)"; done &
disown
