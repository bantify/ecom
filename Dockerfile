FROM ubuntu:latest
LABEL authors="enarban"

ENTRYPOINT ["top", "-b"]
