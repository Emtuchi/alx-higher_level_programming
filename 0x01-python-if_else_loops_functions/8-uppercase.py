#!/usr/bin/python3
def uppercase(str):
    t = ''
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            t = t + chr(ord(i) - 32)
        else:
            t = t + i
    print("{}".format(t))
