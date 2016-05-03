import csv
import pandas as pd
import numpy as np
from csv import writer
import math

nan = float('nan')


def mentalWellBeing():
    df_flourishing = pd.read_csv("StudentLife_AssignmentData/Surveys/FlourishingScale.csv")
    df_loneliness = pd.read_csv("StudentLife_AssignmentData/Surveys/LonelinessScale.csv")
    df_panas = pd.read_csv("StudentLife_AssignmentData/Surveys/panas.csv")
    df_phq = pd.read_csv("StudentLife_AssignmentData/Surveys/PHQ-9.csv")
    df_perceivedStress = pd.read_csv("StudentLife_AssignmentData/Surveys/PerceivedStressScale.csv")


    # print df_flourishing
    # print df_flourishing.columns.values
    list_columns = (df_flourishing.columns.values).tolist()
    list_columns.remove('uid')
    list_columns.remove('type')

    print list_columns
    #raw_input()


    with open("file1.csv", 'w') as f1:
        csvWriter = writer(f1)
        header_list = []
        header_list.append('uid')
        for listItem in list_columns:
            header_list.append(listItem)
        csvWriter.writerow(header_list)
        for index, item in df_flourishing.iterrows():
            temp_uid = item['uid']
            temp_list = []
            temp_list.append(item['uid'])
            for index2, item2 in df_flourishing.iterrows():
                if item2['uid'] == temp_uid and item2['type'] == 'post' and item['type'] == 'pre':
                    for columnValue in list_columns:
                        temp = 0
                        value1 = item[columnValue]
                        #print value1
                        #raw_input()
                        if math.isnan(value1):
                            #print "here"
                            value1 = 0

                        value2 = item2[columnValue]
                        if math.isnan(value2):
                            #print "here"
                            value2 = 0
                        temp = (value1 + value2)/float(2)
                        temp_list.append(temp)
                    csvWriter.writerow(temp_list)
                    continue

    list_columns = []
    list_columns = (df_loneliness.columns.values).tolist()
    list_columns.remove('uid')
    list_columns.remove('type')

    print list_columns
    raw_input()
    with open("file2.csv", 'w') as f1:
        csvWriter = writer(f1)
        header_list = []
        header_list.append('uid')
        header_list.append(x for x in list_columns)
        csvWriter.writerow()
        for index, item in df_flourishing.iterrows():
            temp_uid = item['uid']
            temp_list = []
            temp_list.append(item['uid'])
            for index2, item2 in df_flourishing.iterrows():
                if item2['uid'] == temp_uid and item2['type'] == 'post' and item['type'] == 'pre':
                    for columnValue in list_columns:
                        temp = 0
                        
                        value1 = item[columnValue]
                        #print value1
                        #raw_input()
                        if math.isnan(value1):
                            #print "here"
                            value1 = 0

                        value2 = item2[columnValue]
                        if math.isnan(value2):
                            #print "here"
                            value2 = 0
                        temp = (value1 + value2)/float(2)
                        temp_list.append(temp)
                    csvWriter.writerow(temp_list)
                    continue



if __name__ == '__main__':
    mentalWellBeing()
