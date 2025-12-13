#!/bin/bash

source venv/bin/activate

results=()
for w in air_control
do
  echo "Running $w tests"
  pytest "./$w/"
  results+=("$?")
done

for res in "${results[@]}"; do
  if [[ $res -ne 0 ]]; then
    echo "One or more tests failed"
    exit 1
  fi
done