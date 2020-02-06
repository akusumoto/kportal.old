#!/bin/sh

event_id=$1
user_id=$2
json=$3

token=`cat .login | jq -r .token`

curl -X PUT -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d "${json}" \
        http://localhost:8000/events/${event_id}/users/${user_id}/
