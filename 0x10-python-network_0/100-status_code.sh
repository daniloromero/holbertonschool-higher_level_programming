#!/bin/bash
# sends a request to a URL displays only the status code of the response.
curl -s -o  -w "%{response_code}" "$1"
