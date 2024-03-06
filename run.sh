#!/bin/bash

# Available actions are : clean, extract, build
ACTION=extract
ROOT=$1
TARGET=site_data

python3 -m site_gen $ACTION $ROOT $TARGET

