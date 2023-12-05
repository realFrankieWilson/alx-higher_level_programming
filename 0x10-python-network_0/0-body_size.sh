#!/usr/bin/bash
# A script that prints the lenght of the a url request.
curl -Is "$1" | grep Content-Length: | cut -d ' ' -f2
