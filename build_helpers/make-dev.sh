#!/bin/bash

if [ ! -d "venv" ]; then
  echo "Creating new python env"
  python -m venv venv
fi

source venv/bin/activate

python -m pip install --upgrade pip

for w in air_control
do
  echo "Installing requirements for $w"
  python -m pip install -r "$w/requirements.txt" -q
done
echo "Installing test requirements"
python -m pip install -r ./build_helpers/requirements-test.txt -q

for module in air_control
do
  echo "Installing module $module"
  python -m pip install -e "./$module" -q
done

echo "Installing pre-commit"
python -m pip install pre-commit
pre-commit install -c .pre-commit-config.yaml
