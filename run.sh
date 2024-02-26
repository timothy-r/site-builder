#!/bin/bash

# Available actions are : clean, extract, build
ACTION=clean
ROOT=$1
TARGET=target

python3 -m site_gen $ACTION $ROOT $TARGET