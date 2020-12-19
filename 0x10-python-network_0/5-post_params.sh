#!/bin/bash
# script takes a URL, sends a GET request to URL, displays body of response
curl -sL -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
