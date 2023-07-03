#!/bin/bash
curl -s "$1" -o /dev/null -w "%{http_code}"
