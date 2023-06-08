FROM python:3.11-alpine

RUN mkdir /apps
WORKDIR /apps
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt