#!/bin/sh

event_id=$1
user_id=$2

token=`cat .login | jq -r .token`

curl -X DELETE -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        http://localhost:8000/events/${event_id}/users/${user_id}/
