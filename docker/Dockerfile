FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUMBERBUFFERED=1

WORKDIR /core

COPY sellpy-agent/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY sellpy-agent /core

COPY docker /core/docker