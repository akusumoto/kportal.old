#!/bin/sh

token=`cat .login | jq -r .token`

curl -X POST -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d '{"title":"1st Concert","date":"2020-01-01","open_time":"13:00","start_time":"13:30","place":"Somewhere","detail": "aaa"}' \
        http://localhost:8000/concerts/
