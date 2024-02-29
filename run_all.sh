#!/bin/bash

# Available actions are : clean, extract, build
ACTION=clean
ROOT=$1
TARGET=target

python3 -m site_gen $ACTION $ROOT $TARGET

#!/bin/bash

# Available actions are : clean, extract, build
ACTION=extract
ROOT=target/index.html
TARGET=new_site

python3 -m site_gen $ACTION $ROOT $TARGET

