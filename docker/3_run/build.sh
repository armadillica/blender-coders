#!/usr/bin/env bash

cp ../../requirements.txt .;
docker build -t armadillica/blender_coders -f run.docker .;
rm requirements.txt;
