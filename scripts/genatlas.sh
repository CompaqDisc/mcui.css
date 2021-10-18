#!/bin/bash
# extract.sh - extract enchant glint and other animated items
# genatlas.sh - turn mod-extracted renders into a texture atlas
# makecss.py - run through everything and make some css
montage -tile 32x -geometry +0+0 -background none sprites/* atlas.png
# python scripts/makecss.py sprites/* > sprites.css