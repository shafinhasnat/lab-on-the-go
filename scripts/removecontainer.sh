#!/bin/bash
docker ps --filter name=sshserver-* -aq | xargs docker stop | xargs docker rm
