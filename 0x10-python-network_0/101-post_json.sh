#!/bin/bash
# A post json request.
curl -sH "Content-Type: application/json" -d @"$2" "$1"
