#!/usr/bin/python3
"""
This script fetched data from the url:
https://alx-intranet.hbtn.io/status
"""


import urllib.request


def decode_url():
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    decode_url()
