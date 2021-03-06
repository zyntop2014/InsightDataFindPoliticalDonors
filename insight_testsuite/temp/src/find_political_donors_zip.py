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
import re

def checkValidation(splits):
    zipcodelen =  len(splits[10])  
    zipcode = splits[10]  
    cmte = splits[0]
    amount = splits[14] 
    otherid = splits[15]
    if (otherid  != "" and  otherid  != "NaN" and otherid  != "NaT" \
                                    and otherid  != "NA"):
        #print ("OTHER_ID is not NULL")
        return 0
    if (zipcode  == "" or zipcode  == "NaN" or zipcode  == "NaT" \
                                    and zipcode  != "NA"):
        #print ("ZIP_CODE is NULL")
        return 0
    if (cmte == "" or cmte == "NaN" or cmte == "NaT" \
                                    and cmte != "NA"):
        #print ("CMTE_ID is NULL")
        return 0
    if (amount == "" or amount == "NaN" or amount =="NaT" \
                                    and amount != "NA"):
        #print ("contribution is NULL")
        return 0

    #check digits of the zipcode
    if not re.match("[0-9/]+$", str(zipcode)):
        #print "zipcode are not all the digits"
        return 0
    if (zipcodelen != 9 and zipcodelen != 5):
        print "zipcode len is invalid"
        return 0
    try:
        amount_f = float (amount)
    except ValueError:
        #print ("this is a invalid number of contribution")
        return 0
    return 1

def find_political_donors_zip(input_file, output_file):    
    if os.path.isfile(input_file) and os.access(input_file, os.R_OK):                         
        try:  
            fin = open(input_file, "r")
            file_content = fin.readline()
            fin.close()
            fout = open(output_file, 'w')
            if file_content == "\n":
                print "file is empty with enter line"
                fout.close()
                return None
            if os.stat(input_file).st_size == 0:
                print "file is empty"
                fout.close()
                return None
           
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            fout = open(output_file, 'w')
            fout.close()
            return None
    else:
        print "Either file is missing or is not readable"
        fout = open(output_file, 'w')
        fout.close()
        return None

  
    df_zipcode = pd.DataFrame(columns=['INDEXID','CMTE_ID', 'ZIP_CODE', 'TRANSACTION_MEAN', \
                            'TRANSACTION_COUNT','TRANSACTION_SUM'])
    index =0;
    df_zipcode = df_zipcode.astype(dtype= {"INDEXID": "int64","TRANSACTION_MEAN":"float64", "TRANSACTION_COUNT":"int64","TRANSACTION_SUM":"float64"})
    with open(input_file, "r") as fin:
        for line in fin:
            splits = line.split("|")
            res = checkValidation(splits)
            if (res == 0):
                continue;
            zipcode = splits[10][0:5]
            cmte = splits[0]
            sumvalue = float(splits[14])
            # print df_zipcode
            df_zipcode2= df_zipcode[(df_zipcode.CMTE_ID == cmte) & (df_zipcode.ZIP_CODE == zipcode)]
            
            
            if (df_zipcode2.size == 0):
                indexid = index 
                df_zipcode.loc[index] = [index, cmte, zipcode, sumvalue, 1, sumvalue]  
                index = index + 1
                # print df_zipcode  
            else:
                indexid = df_zipcode2.iloc[0]["INDEXID"]
                pre_sum = df_zipcode2.iloc[0]['TRANSACTION_SUM']

                pre_count = df_zipcode2.iloc[0]['TRANSACTION_COUNT'] 
        
                total_sum = float(sumvalue) + float(pre_sum)
                df_zipcode.loc[indexid, 'TRANSACTION_SUM'] = total_sum
                df_zipcode.loc[indexid, 'TRANSACTION_COUNT'] = int (1 + pre_count)
                df_zipcode.loc[indexid, 'TRANSACTION_MEAN'] = float(total_sum/float(1+pre_count))
                                  
            record = df_zipcode.iloc[indexid]
            mean = str(int(round(record['TRANSACTION_MEAN'])))
            count = str(record['TRANSACTION_COUNT'])
            amount = str(int(record['TRANSACTION_SUM']))
            line = cmte + '|' + zipcode + '|' + mean + '|' + count + '|' + amount  
            try:
                fout.write(line + '\n')
            except:
                print("Unexpected error in writing a output file:", sys.exc_info()[0])  
    fout.close()       
    print "finish write running outputfile : " + output_file
      

def main(argv):
    dir_name = os.path.dirname(os.path.dirname(__file__))  
    if (len(sys.argv) == 1):       
        inputfile = dir_name + "/input/itcont.txt" 
        outfile = dir_name + "/output/medianvals_by_zip.txt"
    elif (len(sys.argv) == 2):
        inputfile = argv[1]
        outfile = dir_name + "/output/medianvals_by_zip.txt"
    else :
        inputfile = argv[1]
        outfile = argv[2]
    print "read inputfile : " + inputfile
    find_political_donors_zip(inputfile, outfile)

if __name__ == "__main__":
    main(sys.argv)





