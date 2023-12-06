#!/bin/bash
# makes a request to /catch_me that causes the server torespond with messages.
curl -sX PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "Origin: HolbertonSchool"
