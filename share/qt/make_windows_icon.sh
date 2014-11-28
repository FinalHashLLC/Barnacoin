#!/bin/bash
# create multiresolution windows icon
ICON_SRC=../../src/qt/res/icons/barnacoin.png
ICON_DST=../../src/qt/res/icons/barnacoin.ico
convert ${ICON_SRC} -resize 16x16 barnacoin-16.png
convert ${ICON_SRC} -resize 32x32 barnacoin-32.png
convert ${ICON_SRC} -resize 48x48 barnacoin-48.png
convert barnacoin-16.png barnacoin-32.png barnacoin-48.png ${ICON_DST}

