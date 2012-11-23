#!/bin/bash

ARCHI=$1
CURDIR=$2
RELEASE=$3
if [[ $ARCHI == *amd64* ]]; then
 ARCH_URL="x86_64"
else
 ARCH_URL="i686"
fi

echo "Downloading Firefox for $ARCHI"
cd $CURDIR/debian/firefox/opt
wget http://releases.mozilla.org/pub/mozilla.org/firefox/releases/latest/linux-$ARCH_URL/en-US/firefox-$RELEASE.tar.bz2
bzip2 -d firefox-$RELEASE.tar.bz2 || exit 1
tar xvf firefox-$RELEASE.tar
rm firefox-$RELEASE.tar
rm firefox/omni.ja
rm -rf firefox/searchplugins/*
rm -rf firefox/defaults/pref/*
cp $CURDIR/searchplugins/* firefox/searchplugins/
cp $CURDIR/pref/* firefox/defaults/pref/
cd $CURDIR

