#!/bin/bash

a2enmod rewrite
/usr/sbin/apache2 -D FOREGROUND
