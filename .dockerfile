# syntax=docker/dockerfile:1

FROM ubuntu:22.0


RUN useradd -m appuser
USER appuser


# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip \
    pip install selenium \
    pip install json \
    pip install numpy \
    pip install pillow 


# install app
COPY passive_teacher /app/passive_teacher


WORKDIR /app/passive_teacher

# final configuration
#ENV FLASK_APP=hello
#EXPOSE 8000
#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
CMD ["echo", "holaaa"]