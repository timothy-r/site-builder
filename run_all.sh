#!/bin/bash

EXTRACT_DIR=target
NEW_SITE_DIR=build_data

rm *.log
rm -r $EXTRACT_DIR
rm -r $NEW_SITE_DIR


# Available actions are : clean, extract, build
ACTION=clean
ROOT=$1
TARGET=$EXTRACT_DIR

python3 -m site_gen $ACTION $ROOT $TARGET

ACTION=extract
ROOT=$TARGET/index.html
TARGET=$NEW_SITE_DIR

python3 -m site_gen $ACTION $ROOT $TARGET

