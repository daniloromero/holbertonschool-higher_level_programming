#!/bin/bash
#sends DELETE request to URL in first argument, displays body of the response
curl -s -X DELETE "$1" 
