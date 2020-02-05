#!/bin/sh

curl -X POST -H 'Content-Type: application/json' \
        -d '{"username":"CB_AKIRA","password":"password123"}' \
        http://localhost:8000/login/ > .login 2>/dev/null
