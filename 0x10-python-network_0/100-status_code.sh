#!/bin/bash
# Send a request to the URL passed as an argument and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
