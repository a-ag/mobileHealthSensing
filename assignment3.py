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
                        try:
                            value1 = item[columnValue]
                        except:
                            value1=0
                        #print value1
                        #raw_input()
                        if math.isnan(value1):
                            #print "here"
                            #raw_input('nan')
                            value1 = 0

                        try:
                            value2 = item2[columnValue]
                        except:
                            value2=0
                        temp = (value1 + value2)/float(2)
                        temp_list.append(temp)
                    csvWriter.writerow(temp_list)
                    continue

    list_columns = []
    list_columns = (df_loneliness.columns.values).tolist()
    list_columns.remove('uid')
    list_columns.remove('type')

    print list_columns
    #raw_input()
    with open("file2.csv", 'w') as f1:
        csvWriter = writer(f1)
        header_list = []
        header_list.append('uid')
        for listItem in list_columns:
            header_list.append(listItem)
        csvWriter.writerow(header_list)
        for index, item in df_loneliness.iterrows():
            temp_uid = item['uid']
            temp_list = []
            temp_list.append(item['uid'])
            for index2, item2 in df_loneliness.iterrows():
                if item2['uid'] == temp_uid and item2['type'] == 'post' and item['type'] == 'pre':
                    for columnValue in list_columns:
                        #print columnValue
                        #print item[columnValue]
                        temp = 0
                        dict = {
                            'never':0,
                            'rarely':1,
                            'sometimes':2,
                            'often':3,
                            '':0,
                            ' ':0
                        }
                        try:
                            value1 = dict[item[columnValue].lower()]
                        except:
                            value1=0
                        #print value1
                        #raw_input()
                        if math.isnan(value1):
                            #print "here"
                            #raw_input('nan')
                            value1 = 0

                        try:
                            value2 = dict[item2[columnValue].lower()]
                        except:
                            value2=0
                        temp = (value1 + value2)/float(2)
                        temp_list.append(temp)
                    csvWriter.writerow(temp_list)
                    continue
    list_columns = []
    list_columns = (df_perceivedStress.columns.values).tolist()
    list_columns.remove('uid')
    list_columns.remove('type')

    print list_columns
    #raw_input()
    with open("file3.csv", 'w') as f1:
        csvWriter = writer(f1)
        header_list = []
        header_list.append('uid')
        for listItem in list_columns:
            header_list.append(listItem)
        csvWriter.writerow(header_list)
        for index, item in df_perceivedStress.iterrows():
            temp_uid = item['uid']
            temp_list = []
            temp_list.append(item['uid'])
            for index2, item2 in df_perceivedStress.iterrows():
                if item2['uid'] == temp_uid and item2['type'] == 'post' and item['type'] == 'pre':
                    for columnValue in list_columns:
                        #print columnValue
                        #print item[columnValue]
                        #print item2['uid']
                        #print columnValue
                        temp = 0
                        dict = {
                            'never':0,
                            'almost never':1,
                            'sometime':2,
                            'fairly often':3,
                            'very often':4
                            # '':0,
                            # ' ':0
                        }
                        # if math.isnan(item[columnValue]):
                        #     print "nana"
                        try:
                            value1 = dict[item[columnValue].lower()]
                        except:
                            value1=0
                        #print value1
                        #raw_input()
                        if math.isnan(value1):
                            #print "here"
                            #raw_input('nan')
                            value1 = 0

                        try:
                            value2 = dict[item2[columnValue].lower()]
                        except:
                            value2=0
                        if math.isnan(value2):
                            #print "here"
                            value2 = 0
                        temp = (value1 + value2)/float(2)
                        temp_list.append(temp)
                    csvWriter.writerow(temp_list)
                    continue
    list_columns = []
    list_columns = (df_phq.columns.values).tolist()
    list_columns.remove('uid')
    list_columns.remove('type')

    print list_columns
    #raw_input()
    with open("file4.csv", 'w') as f1:
        csvWriter = writer(f1)
        header_list = []
        header_list.append('uid')
        for listItem in list_columns:
            header_list.append(listItem)
        csvWriter.writerow(header_list)
        for index, item in df_phq.iterrows():
            temp_uid = item['uid']
            temp_list = []
            temp_list.append(item['uid'])
            for index2, item2 in df_phq.iterrows():
                if item2['uid'] == temp_uid and item2['type'] == 'post' and item['type'] == 'pre':
                    for columnValue in list_columns:
                        #print columnValue
                        #print item[columnValue]
                        #print item['uid']
                        #print columnValue
                        temp = 0
                        dict = {
                            'not at all':0,
                            'several days':1,
                            'more than half the days':2,
                            'nearly every day':3,
                            'not difficult at all':0,
                            'somewhat difficult':1,
                            'very difficult':2,
                            'extremely difficult':3

                        }
                        try:
                            value1 = dict[item[columnValue].lower()]
                        except:
                            value1=0
                        #print value1
                        #raw_input()
                        if math.isnan(value1):
                            #print "here"
                            #raw_input('nan')
                            value1 = 0

                        try:
                            value2 = dict[item2[columnValue].lower()]
                        except:
                            value2=0
                        temp = (value1 + value2)/float(2)
                        temp_list.append(temp)
                    csvWriter.writerow(temp_list)
                    continue

    list_columns=[]
    list_columns = (df_panas.columns.values).tolist()
    list_columns.remove('uid')
    list_columns.remove('type')

    print list_columns
    #raw_input()


    with open("file5.csv", 'w') as f1:
        csvWriter = writer(f1)
        header_list = []
        header_list.append('uid')
        for listItem in list_columns:
            header_list.append(listItem)
        csvWriter.writerow(header_list)
        for index, item in df_panas.iterrows():
            temp_uid = item['uid']
            temp_list = []
            temp_list.append(item['uid'])
            for index2, item2 in df_panas.iterrows():
                if item2['uid'] == temp_uid and item2['type'] == 'post' and item['type'] == 'pre':
                    for columnValue in list_columns:
                        temp = 0
                        try:
                            value1 = item[columnValue]
                        except:
                            value1=0
                        #print value1
                        #raw_input()
                        if math.isnan(value1):
                            #print "here"
                            #raw_input('nan')
                            value1 = 0

                        try:
                            value2 = item2[columnValue]
                        except:
                            value2=0
                        temp = (value1 + value2)/float(2)
                        temp_list.append(temp)
                    csvWriter.writerow(temp_list)
                    continue

    df1 = pd.read_csv("file1.csv")
    df2 = pd.read_csv("file1.csv")
    df3 = pd.read_csv("file1.csv")
    df4 = pd.read_csv("file1.csv")
    df5 = pd.read_csv("file1.csv")

    df1 = df1.set_index('uid')
    # print df1
    df2 = df2.set_index('uid')
    df3 = df3.set_index('uid')
    df4 = df4.set_index('uid')
    df5 = df5.set_index('uid')

    result = pd.concat([df1,df2,df3,df4,df5],axis=1,join='inner')

    result.to_csv("output.csv")


if __name__ == '__main__':
    mentalWellBeing()
