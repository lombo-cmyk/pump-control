FROM python:3.11-bookworm

WORKDIR /usr/src/app

# Move the requirements files first
# If they're the same - pip installation will used cached data and speed up building
COPY ./air_control/requirements.txt requirements/service.txt
RUN pip install -r ./requirements/service.txt

COPY ./air_control/ air_control/

RUN pip install ./air_control

ENV TZ="Europe/Warsaw"

CMD [ "python", "-m", "air_control" ]