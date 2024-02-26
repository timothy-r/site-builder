#!/bin/bash

# Available actions are : clean, extract, build
ACTION=extract
ROOT=$1
TARGET=new_site

python3 -m site_gen $ACTION $ROOT $TARGET