#!/bin/sh

id=$1
#json='{"value": "遅刻"}'
json=$2

token=`cat .login | jq -r .token`

curl -X POST -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d "${json}" \
        http://localhost:8000/events/${id}/answers/
