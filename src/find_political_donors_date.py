# -*- coding: utf-8 -*-
"""
Author : Yanan Zhang
Date: 10/27/2017
Purpose: Insight Data Code Challege

"""
import datetime as dt
import numpy as np
import pandas as pd
import os.path
import sys

def parseDate(x):
    try:
        return dt.datetime.strptime(x,'%m%d%Y')
    except ValueError:
        return np.datetime64('NaT')

def find_political_donors_date(inputfile, outfile):
    dir_name = os.path.dirname(os.path.dirname(__file__)) 
    input_file = dir_name + inputfile 
    output_file = dir_name + outfile
    
    if os.path.isfile(input_file) and os.access(input_file, os.R_OK):
        try:  
            fin = open(input_file, "r")
            file_content = fin.readline()
            fin.close()
            if file_content == "\n":
                print "file is empty with enter line"
                fout = open(output_file, 'w')
                fout.close()
                return None
            if os.stat(input_file).st_size == 0:
                print "file is empty"
                fout = open(output_file, 'w')
                fout.close()
                return None
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            fout = open(output_file, 'w')
            fout.close()
            return None
        df = pd.read_table(input_file, sep='|', header=None, dtype={13: str}, \
                       low_memory=False)
    else:
        print "Either file is missing or is not readable"
        fout = open(output_file, 'w')
        fout.close()
        return None
                 
    df1 = df[[0, 13, 14, 15]]
    df1.columns = ['CMTE_ID', 'TRANSACTION_DT', 'TRANSACTION_AMT',
                       'OTHER_ID']
    df_date = df1[(df1['OTHER_ID'].isnull()) & \
                  (df1['TRANSACTION_DT'].notnull()) & \
                  (df1['TRANSACTION_DT'].str.isdigit()) & \
                  (df1['CMTE_ID'].notnull()) & \
                  (df1['TRANSACTION_AMT'].notnull())]
    mask = (df_date['TRANSACTION_DT'].str.len() == 8) 
    df_date = df_date.loc[mask]
    df_date['TRANSACTION_COUNT'] = df_date['TRANSACTION_AMT']
    df_date['TRANSACTION_SUM'] = df_date['TRANSACTION_AMT']
    df = df_date.groupby(['CMTE_ID', 'TRANSACTION_DT'])\
                        .agg({'TRANSACTION_AMT': 'mean', \
                        'TRANSACTION_COUNT':'count', \
                        'TRANSACTION_SUM':'sum' })\
                        .reset_index()\
                        .rename(columns={'TRANSACTION_AMT':'TRANSACTION_MEAN'}) 
        
    df['TRANSACTION_MEAN'] = df['TRANSACTION_MEAN'].round(0).astype(np.int64)
    df['TRANSACTION_DT2'] = df['TRANSACTION_DT'].apply(lambda x: parseDate(x))
    df = df[(df['TRANSACTION_DT2'].notnull())]
    df = df.sort_values(by = ['CMTE_ID','TRANSACTION_DT2'])
    df_out = df[['CMTE_ID', 'TRANSACTION_DT', 'TRANSACTION_MEAN', \
    			'TRANSACTION_COUNT', 'TRANSACTION_SUM']]
    try:
        np.savetxt(output_file, df_out.values, fmt='%s', delimiter = "|")
        print "write outputfile : " + outfile
    except:
        print("Unexpected error in writing a output file:", sys.exc_info()[0])  
  
def main(argv):
    if (len(sys.argv) == 1):
        inputfile = "/input/itcont.txt" 
        outfile = "/output/medianvals_by_date.txt";
    elif (len(sys.argv) == 2):
        inputfile = argv[1]
        outfile = "/output/medianvals_by_date.txt";
    else :
        inputfile = argv[1]
        outfile = argv[2]    
    print "read inputfile : " + inputfile
    find_political_donors_date(inputfile, outfile)


if __name__ == "__main__":
    main(sys.argv)
 





