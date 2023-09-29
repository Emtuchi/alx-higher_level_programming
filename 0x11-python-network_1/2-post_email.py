#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    """create a dictionary 'values' with email as a key"""
    values = {'email': sys.argv[2]}
    """encode the dic into a url-encoded string"""
    data = parse.urlencode(values)
    """encode the url-encoded string as ascii bytes"""
    data = data.encode('ascii')
    """create a http post request with the url and data"""
    req = request.Request(sys.argv[1], data)
    """use urllib.request.urlopen() to send the post request"""
    with request.urlopen(req) as response:
        """read and store the body of the http response as
           'body'"""
        body = response.read()
        print(body.decode('utf-8'))
