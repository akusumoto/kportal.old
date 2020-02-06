#!/bin/sh

id=$1
json=$2

token=`cat .login | jq -r .token`

curl -X PUT -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d "${json}" \
        http://localhost:8000/events/${id}/
