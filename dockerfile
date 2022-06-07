FROM ubuntu:21.10

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Istanbul

RUN apt-get update && apt-get install -y \
    python \
    python3 \
    python3-pip 

COPY . .

ENTRYPOINT ["tail"]

CMD ["-f","/dev/null"]

# RUN pip install --requirement /tmp/requirements.txt