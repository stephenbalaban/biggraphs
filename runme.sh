#!/bin/bash
if [[ $1 ]]; then
    if [[ $2 ]]; then
	X=$1
	Y=$2
    fi;

    outfile=graphvizDOT_$X-$Y.txt

    # make output file
    python gen.py $X $Y > $outfile
    # make graphviz graph
    ./show.sh $outfile out/out_$X-$Y.png
    rm $outfile
else
    echo "usage: ./runme.sh X Y"
fi;
