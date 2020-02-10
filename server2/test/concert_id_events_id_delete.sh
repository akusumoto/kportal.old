#!/bin/sh

concert_id=$1
event_id=$2

token=`cat .login | jq -r .token`

curl -X DELETE -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        http://localhost:8000/concerts/${concert_id}/events/${event_id}/
