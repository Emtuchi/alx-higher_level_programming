#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys


if __name__ == "__main__":
    """get url from command line"""
    url = sys.argv[1]

    """get the http headers from the response, using
       response.info()"""
    headers = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
