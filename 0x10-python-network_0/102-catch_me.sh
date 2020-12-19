#!/bin/bash
# script sends DELETE request 2 URL passed as argument,displays body response
curl -sL -X PUT -d "user_id=98" "HolbertonSchool" 0.0.0.0:5000/catch_me 
