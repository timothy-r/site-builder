#!/bin/bash

# Available actions are : clean, extract, build
ACTION=clean
ROOT=$1
TARGET=target

python3 -m site $ACTION $ROOT $TARGET