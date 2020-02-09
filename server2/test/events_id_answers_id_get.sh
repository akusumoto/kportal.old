#!/bin/sh

event_id=$1
answer_id=$2

token=`cat .login | jq -r .token`

curl -X GET -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        http://localhost:8000/events/${event_id}/answers/${answer_id}/
