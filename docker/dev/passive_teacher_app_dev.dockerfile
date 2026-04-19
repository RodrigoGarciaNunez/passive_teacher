# syntax=docker/dockerfile:1

FROM ubuntu:25.10
ARG REQUIREMENTS_FILE
ARG APP_MAIN_DIR


# install app dependencies
RUN  apt-get update && apt-get install -y python3 python3-pip 

COPY ./requirements.txt / 

RUN pip install --no-cache-dir -r requirements.txt  --break-system-packages

RUN useradd -m appuser
USER appuser

#Set workdir
WORKDIR /app/passive_teacher



EXPOSE 8050
#CMD ["tail","-f","/dev/null"]