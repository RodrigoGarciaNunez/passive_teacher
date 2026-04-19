# syntax=docker/dockerfile:1

# 1. Build stage
FROM python:3.11-slim AS builder

ARG REQUIREMENTS_FILE
#ARG APP_MAIN_DIR

WORKDIR /build

RUN apt-get update && apt-get install -y build-essential

COPY ${REQUIREMENTS_FILE} requirements.txt

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# 2. Runtime stage
FROM python:3.11-slim

ARG APP_MAIN_DIR

RUN useradd -m appuser

WORKDIR /app/passive_teacher

COPY --from=builder /install /usr/local

COPY ${APP_MAIN_DIR}/view /app/passive_teacher/view
COPY ${APP_MAIN_DIR}/controller /app/passive_teacher/controller

WORKDIR /app/passive_teacher

#se bajan los privilegios
USER appuser 
