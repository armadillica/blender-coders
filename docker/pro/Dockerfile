FROM ubuntu:14.04

MAINTAINER Francesco Siddi <francesco@blender.org>

RUN apt-get update && apt-get install -y \
python \
python-dev \
python-pip \
nano \
software-properties-common \
apache2-mpm-event \
libapache2-mod-wsgi

# Enable apache mods.
RUN a2enmod rewrite

RUN mkdir -p /data/git/blender-coders

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

RUN pip install virtualenv \
&& virtualenv /data/venv

ENV PIP_PACKAGES_VERSION 1
ADD requirements.txt /requirements.txt

RUN . /data/venv/bin/activate && pip install -r /requirements.txt \
&& rm /requirements.txt

VOLUME /data/git/blender-coders
VOLUME /data/git/letsencrypt

ENV IS_DOCKER True

EXPOSE 80

ADD 000-default.conf /etc/apache2/sites-available/000-default.conf
ADD runserver.sh /runserver.sh

ENTRYPOINT ["bash", "/runserver.sh"]
