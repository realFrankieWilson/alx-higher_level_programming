#!/bin/bash
# A script that prints the lenght of the a url request.
curl -s "$1" | wc -c
