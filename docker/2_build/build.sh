#!/usr/bin/env bash

mkdir -p ../3_run/wheelhouse;
cp ../../requirements.txt .;

docker build -t blender_coders_build -f build.docker .;
docker run --rm \
       -v "$(pwd)"/../3_run/wheelhouse:/data/wheelhouse \
       blender_coders_build;

rm requirements.txt;
