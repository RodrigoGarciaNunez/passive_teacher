FROM ubuntu:25.10


RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN  apt-get update && apt-get install -y python3 python3-pip 
COPY ./requirements.txt / 
RUN pip install --no-cache-dir -r requirements.txt  --break-system-packages


WORKDIR /app/passive_teacher/



