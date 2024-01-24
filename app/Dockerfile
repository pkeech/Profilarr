## DEFINE BASE IMAGE
FROM python:3.11.7-slim-bullseye as base

## DEFINE WORKING DIRECTORY
WORKDIR /app/profilarr

## COPY REQUIRED FILES
COPY . /app/profilarr/

## INSTALL REQUIREMENTS
RUN pip install -r requirements.txt \
    && rm requirements.txt

## DEFINE EXPOSED PORT
EXPOSE 8080

## DEFINE VOLUME
VOLUME ["/app/profilarr/data"]

## DEFINE DEVELOPMENT IMAGE
FROM base as dev

## DEFINE ENTRYPOINT / COMMAND
CMD ["flask", "run", "--host=0.0.0.0"]

## DEFINE RELEASE IMAGE
FROM base as release

## DEFINE ENTRYPOINT / COMMAND