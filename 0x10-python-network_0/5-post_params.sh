#!/bin/bash
# Sends a POST request to the passed url, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will allways bei herei fori PLD"  "$1"
