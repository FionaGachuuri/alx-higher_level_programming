#!/usr/bin/python3
"""
This script... fetches an Url and displays  value of e
X-Request-Id variable found in the header of the response
"""

import urllib.request
import sys


def main():
    """
    Fetch the URL passed as an argument
    and display the X-Request-Id header.
    """
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == '__main__':
    main()
