#Insight Date Challenge
This is the directory where your program would find any test input files.

Purpose: This is a project for Insight Data Code Callenge

Submit files:

The python script is placed under the src folder. 

1. find_political_donors_zip.py
this is the file to solve the first part. It implements the challenge 1, which is to read the input data from txt and calcalate the running mean for the individual contribvutions. The output is placed under /output/medianvals_by_zip.txt. It contains a calculated running median, total dollar amount and total number of contributions by recipient and zip code.

2. find_political_donors_date.py
The second script find_political_donors_zip.py computes the sum, mean and count of the contributions for each combination of date and receiptant. The output file is medianvals_by_date.txt placed in the path of /output/medianvals_by_date.txt  has the calculated median, total dollar amount and total number of contributions by recipient and date.


Tools:
This script makes use of the following libraries of python and the python version is 2.7.13.
1. pandas
2. numpy 

Tests:
I added up to 10 test suits to test the python code. The tests take into the considerations as described in the readme of the data challenge website. For each test suit, there is a readme.md to describe the test suit purpose.

Run:
A bash script called run.sh in the root directory could be used to run both of the two python files.




