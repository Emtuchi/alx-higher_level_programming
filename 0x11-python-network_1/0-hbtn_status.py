#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
        import urllib.request
        """import this module, which provides functions
           for opening urls"""

        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
            """open the specified url and assign the response to res,
               the 'with' statement is used here to ensure that the response
               is properly after use"""
            content = res.read()
            '''read the response and store the result in 'content' variable'''
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
            """decode the content as utf-8 and print it. this converts the bytes
               to a string for human-readable output"""
