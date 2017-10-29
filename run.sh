#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
chmod a+x ./src/find_political_donors_date.py
chmod a+x ./src/find_political_donors_zip.py

python ./src/find_political_donors_date.py /input/itcont.txt  /output/medianvals_by_date.txt
python ./src/find_political_donors_zip.py /input/itcont.txt /output/medianvals_by_zip.txt 

