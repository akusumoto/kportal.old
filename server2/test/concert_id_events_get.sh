#!/bin/sh

id=$1

token=`cat .login | jq -r .token`

curl -X GET -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        http://localhost:8000/concerts/${id}/events/
