#!/usr/bin/env bash

if [ "$DEV" = "true" ]; then
    echo "Running in development mode"
    . /data/venv/bin/activate && python /data/git/blender-coders/blender-coders/app.py
else
    # Run Apache
    a2enmod rewrite
    /usr/sbin/apache2ctl -D FOREGROUND
fi
