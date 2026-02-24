# syntax=docker/dockerfile:1

FROM ubuntu:25.10



# install app dependencies
RUN  apt-get update && apt-get install -y python3 python3-pip \ 
    chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /

RUN python3 -m pip install --no-cache-dir -r requirements.txt --break-system-packages


RUN useradd -m appuser
USER appuser

# install app
COPY . /app/passive_teacher
WORKDIR /app/passive_teacher
USER root
RUN chmod +x passive_teacher.sh

USER appuser


# final configuration

#ENV FLASK_APP=hello
#EXPOSE 8000
#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
CMD ["./passive_teacher.sh", "-d", "test_resouces/test_dir.xlsx"]