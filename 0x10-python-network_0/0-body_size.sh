#!/usr/bin/env bash
# A script that prints the lenght of the a url request.
resp=$(curl -s -w "%{size_download}" -o /dev/null "$1") && echo "$resp"
