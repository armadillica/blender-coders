#!/usr/bin/env bash

set -x;
set -e;

cd 1_base/;
bash build.sh;

cd ../2_build/;
bash build.sh;

cd ../3_run/;
bash build.sh;
