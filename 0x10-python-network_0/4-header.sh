#!/bin/bash
# Script to send a GET request with a custom header and display the response body
curl -s -H "X-School-User-Id: 98" "$1"
