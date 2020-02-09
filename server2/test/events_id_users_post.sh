#!/bin/sh

event_id=$1
#json='{"id":"4","answer":{"id":"1"},"comment":"TEST"}'
json=$2

token=`cat .login | jq -r .token`

curl -X POST -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d "${json}" \
        http://localhost:8000/events/${event_id}/users/
