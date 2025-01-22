#!/usr/bin/python3
"""
The script sendss a  post request to URL with e email paraameters
and dispalys body of e response .
"""


import urllib.request
import urllib.parse
import sys


def main():
    """
    Send a POST request with an email parameter and display the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == '__main__':
    main()
