FROM ubuntu:14.04
MAINTAINER Francesco Siddi <francesco@blender.org>

RUN apt-get update && apt-get install -y \
python \
python-dev \
python-pip \
nano

RUN mkdir -p /data/git/blender-coders

RUN pip install virtualenv \
&& virtualenv /data/venv

ENV PIP_PACKAGES_VERSION 2
ADD requirements.txt /requirements.txt

RUN . /data/venv/bin/activate \
&& pip install -r /requirements.txt

VOLUME /data/git/blender-coders

EXPOSE 5000

ENV BUILD_VERSION 1

ADD runserver.sh /runserver.sh

ENTRYPOINT ["bash", "/runserver.sh"]
