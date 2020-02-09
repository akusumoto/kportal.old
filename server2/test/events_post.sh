#!/bin/sh

token=`cat .login | jq -r .token`

curl -X POST -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d '{"date":"2020-01-01","place":"Somewhere","subject":"Event1","detail": "aaa","answers":[{"value":"Yes"},{"value":"No"}],"users":[{"id":"1"},{"id":"2"}]}' \
        http://localhost:8000/events/
