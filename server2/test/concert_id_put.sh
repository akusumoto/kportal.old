#!/bin/sh

id=$1
#json='{"id":2,"title":"1st Concert","date":"2020-01-01","open_time":"13:00:00","start_time":"13:30:00","place":"Somewhere","detail":"aaa","status":"active"}'
json=$2

token=`cat .login | jq -r .token`

curl -X PUT -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d "${json}" \
        http://localhost:8000/concerts/${id}/
