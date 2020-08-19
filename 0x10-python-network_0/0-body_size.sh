#!/bin/bash
# sends request to that URL, and displays the size of the body of the response
curl -sI "S1" | grep "Content-Lenght:" | cut -d ' ' -f2
