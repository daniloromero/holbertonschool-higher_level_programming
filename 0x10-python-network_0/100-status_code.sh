#!/bin/bash
# sends a request to a URL displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
