#!/bin/bash
# a script that sends a GET request to a URL with the header variable X-School-User-Id as 98
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
