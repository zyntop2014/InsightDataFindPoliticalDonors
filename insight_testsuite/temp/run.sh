#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
chmod a+x ./src/find_political_donors_date.py
chmod a+x ./src/find_political_donors_zip.py

BASEDIR=$(dirname "$0")
echo "$BASEDIR"

python ./src/find_political_donors_date.py $BASEDIR/input/itcont.txt  $BASEDIR/output/medianvals_by_date.txt
python ./src/find_political_donors_zip.py $BASEDIR/input/itcont.txt $BASEDIR/output/medianvals_by_zip.txt 

