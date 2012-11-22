#!/bin/bash

ARCHI=`getconf LONG_BIT`
if [[ $ARCHI == *64* ]]; then
 ARCHI="amd64"
 ARCH_URL="x86_64"
else
 ARCHI="i386"
 ARCH_URL="i686"
fi

mkdir -p opt
rm -rf opt/*
cd opt
wget --quiet -nd -r -l1 --no-parent -A "*.bz2" http://releases.mozilla.org/pub/mozilla.org/firefox/releases/latest/linux-$ARCH_URL/en-US/

RELEASE=`ls firefox* | cut -d "-" -f2 | sed "s/.tar.bz2//"`
bzip2 -d firefox-$RELEASE.tar.bz2
tar xf firefox-$RELEASE.tar
rm firefox-$RELEASE.tar
rm firefox/omni.ja
cd ..

echo "Downloaded Firefox $RELEASE for $ARCHI"

rm -rf opt/firefox/searchplugins/*
cp searchplugins/* opt/firefox/searchplugins/
rm -rf opt/firefox/defaults/pref/*
cp pref/* opt/firefox/defaults/pref/

rm -rf opt/robots.txt

