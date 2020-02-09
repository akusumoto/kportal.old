#!/bin/sh

# json='{"username":"CB_AKIRA2","email":"gkusumoto@gmail.com","name":"Akira Kusumoto","nickname":"アキラ2","password":"password123","part":"vn1"}'
json=$1

token=`cat .login | jq -r .token`

curl -X POST -H 'Content-Type: application/json' \
        -H "Authorization: JWT ${token}" \
        -d "${json}" \
        http://localhost:8000/member/users/
