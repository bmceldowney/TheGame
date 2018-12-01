#!/bin/bash

#####################################
#
# Installer script for kivent modules
# Author: Meet Udeshi
#
#####################################

############ CONFIG ###########
BRANCH='master' # change to whichever you want

# Install cymunk for kivent_cymunk
pip install git+https://github.com/tito/cymunk

cd /tmp
git clone -b $BRANCH https://github.com/kivy/kivent
cd kivent/modules

pip install ./core
pip install ./cymunk
pip install ./particles
pip install ./projectiles
pip install ./maps

echo "Done installing kivent"