#!/bin/bash
# script takes a URL and displays all HTTP methods the server will accept
curl -sL -IX OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2- 
