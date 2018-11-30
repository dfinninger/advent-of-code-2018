#!/bin/bash

set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: $0 <day_num>"
fi

basedir=`dirname $0`
target_file=$basedir/days/day_"${1}".py

if [ -f "${target_file}" ]; then
  echo "${target_file} exists!"
  exit 1
fi

sed "s/{{day}}/${1}/g" template.py > "${target_file}"

