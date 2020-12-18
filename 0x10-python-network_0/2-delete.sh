#!/bin/bash
# script sends DELETE request 2 URL passed as argument,displays body response
curl -sL -X DELETE "$1"
