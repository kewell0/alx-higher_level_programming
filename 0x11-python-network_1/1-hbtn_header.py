#!/usr/bin/python3
"""  Takes in a URL sends a request and displays the value the X-Request-Id """
import urllib.request as request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as reply:
        html = reply.read()
        print("{}".format(reply.info().get("X-Request-Id")))
