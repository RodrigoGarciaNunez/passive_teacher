# syntax=docker/dockerfile:1

FROM ubuntu:25.10



# install app dependencies
RUN  apt-get update && apt-get install -y python3 python3-pip \ 
    chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/* 
    #curl -LsSf https://astral.sh/uv/install.sh | sh 
    #snap install astral-uv --classic   


COPY ${ENV_FILE} / 


RUN pip install --no-cache-dir -r  --break-system-packages


RUN useradd -m appuser
USER appuser

# # install app
#COPY . /app/passive_teacher
WORKDIR /app/passive_teacher
# USER root
# RUN chmod +x passive_teacher.sh

# USER appuser


# #final configuration

# ENV FLASK_APP=hello
EXPOSE 8050
#CMD ["tail","-f","/dev/null"]