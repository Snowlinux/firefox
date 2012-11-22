#!/bin/bash

ARCHI=$1
CURDIR=$2
if [[ $ARCHI == *amd64* ]]; then
 ARCH_URL="x86_64"
else
 ARCH_URL="i686"
fi

echo "Downloading Firefox for $ARCHI"
cd $CURDIR/debian/firefox/opt
wget -nd -r -l1 --no-parent -A "*.bz2" http://releases.mozilla.org/pub/mozilla.org/firefox/releases/latest/linux-$ARCH_URL/en-US/
mv *bz2 firefox.tar.bz2
bzip2 -d firefox.tar.bz2
tar xvf firefox.tar
rm firefox.tar
rm firefox/omni.ja
rm -rf firefox/searchplugins/*
rm -rf firefox/defaults/pref/*
rm -rf opt/robots.txt
cp $CURDIR/searchplugins/* firefox/searchplugins/
cp $CURDIR/pref/* firefox/defaults/pref/
cd $CURDIR

