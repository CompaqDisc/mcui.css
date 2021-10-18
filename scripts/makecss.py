#!/usr/bin/env python3
# usage: scripts/makecss.py sprites/* > sprites.css
import sys
import os
from string import Template

files = sys.argv[1:]
if len(files) == 0:
    exit()

print('''
.mcui-sprite {
    width: 32px;
    height: 32px;
    vertical-align: middle;

    display: inline-block;
    background-repeat: no-repeat;

    background-image: url('images/atlas.png');
}
''')

template = Template('''
.mcui-sprite[data-id="$id"] {
    background-position: -$x -$y;
}
''')

for path in files:
    y = str(int(files.index(path) / 32) * 32) + "px"
    x = str(int((files.index(path) * 32) % (32*32))) + "px"
    name = os.path.basename(path)[10:-4]
    s = template.safe_substitute(id=name, x=x, y=y)
    print(s)
