#!/bin/bash
#sends DELETE request to URL in first argument, displays body of the response
curl -X DELETE "$1" 
