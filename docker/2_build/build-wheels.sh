#!/usr/bin/env bash

. /data/venv/bin/activate && pip wheel --wheel-dir=/data/wheelhouse -r /requirements.txt
