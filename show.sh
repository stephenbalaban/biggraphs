#!/bin/bash
if [[ $1 ]]; then
    sfdp -Tpng -o $2 $1;
    open $2
else
    echo "usage: ./show <input> <output>"
fi;