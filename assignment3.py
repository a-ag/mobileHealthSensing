import csv
import pandas as pd
import numpy as np
from csv import writer
import math
import collections
from statsmodels.sandbox.regression.predstd import wls_prediction_std

nan = float('nan')


def mentalWellBeing():
    df_flourishing = pd.read_csv("StudentLife_AssignmentData/Surveys/FlourishingScale.csv",index_col=False)
    df_loneliness = pd.read_csv("StudentLife_AssignmentData/Surveys/LonelinessScale.csv",index_col=False)
    df_panas = pd.read_csv("StudentLife_AssignmentData/Surveys/panas.csv",index_col=False)
    df_phq = pd.read_csv("StudentLife_AssignmentData/Surveys/PHQ-9.csv",index_col=False)
    df_perceivedStress = pd.read_csv("StudentLife_AssignmentData/Surveys/PerceivedStressScale.csv",index_col=False)


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

    df1 = pd.read_csv("file1.csv",index_col=False)
    df2 = pd.read_csv("file1.csv",index_col=False)
    df3 = pd.read_csv("file1.csv",index_col=False)
    df4 = pd.read_csv("file1.csv",index_col=False)
    df5 = pd.read_csv("file1.csv",index_col=False)

    df1 = df1.set_index('uid')
    # print df1
    df2 = df2.set_index('uid')
    df3 = df3.set_index('uid')
    df4 = df4.set_index('uid')
    df5 = df5.set_index('uid')

    result = pd.concat([df1,df2,df3,df4,df5],axis=1,join='inner')

    result.to_csv("output_mentalWellBeing.csv")

def socialEngagement():
    counter = 0

    with open("socialEngagement.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(['uid','total_calls','total_conversations','mean_call_duration','std_call_duration'])

    while counter<=60:
        counter+=1
        temp_list = []

        if counter < 10:
            user_id = 'u0' + str(counter)
        else:
            user_id = 'u' + str(counter)

        temp_list.append(user_id)

        total_calls = 0
        try:
            df = pd.read_csv('StudentLife_AssignmentData/SensingData/CallLog/call_log_' + user_id + '.csv',index_col=False)
        except:
            continue
        total_calls = len(df)
        temp_list.append(total_calls)

        try:
            df = pd.read_csv('StudentLife_AssignmentData/SensingData/Conversations/conversation_' + user_id + '.csv',index_col=False)
        except:
            continue
        total_conversations = 0
        total_conversations=len(df)
        temp_list.append(total_conversations)

        list_timeDiff = []
        print df.columns.values
        for index,item in df.iterrows():
            list_timeDiff.append(item[' end_timestamp']-item['start_timestamp'])
        mean_call_duation = np.mean(list_timeDiff)
        std_call_duration = np.std(list_timeDiff)

        temp_list.append(mean_call_duation)
        temp_list.append(std_call_duration)

        with open("socialEngagement.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(temp_list)

def mobility():
    counter = 0

    with open("mobility.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(['uid','total_location','unique_location'])

    while counter<=60:
        counter+=1
        temp_list = []

        if counter < 10:
            user_id = 'u0' + str(counter)
        else:
            user_id = 'u' + str(counter)

        temp_list.append(user_id)

        total_locations = 0
        try:
            df = pd.read_csv('StudentLife_AssignmentData/SensingData/Wifi_Location/wifi_location_' + user_id + '.csv',index_col=False)
        except:
            continue
        #print df
        total_locations=len(df)
        #print total_locations
        temp_list.append(total_locations)
        list_locations = []

        list_locations=df['location'].tolist()
        # for index, item in df.iterrows():
        #     #print type(item['location'])
        #     #print item
        #     #raw_input()
        #     list_locations.append(item['location'])

        set_locations = set(list_locations)

        #print len(list_locations)

        # for item in list_locations:
        #     print item
            #raw_input()
        #print len(set_locations)
        #raw_input()

        temp_list.append(len(set_locations))
        #raw_input()
        with open("mobility.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(temp_list)

def activity():
    counter = 0

    with open("physical_activity.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(['uid','most_freq_activity','proportion_running_walking'])

    while counter<=60:
        counter+=1
        temp_list = []

        if counter < 10:
            user_id = 'u0' + str(counter)
        else:
            user_id = 'u' + str(counter)

        temp_list.append(user_id)


        try:
            df = pd.read_csv('StudentLife_AssignmentData/SensingData/PhysicalActivity/activity_' + user_id + '.csv',index_col=False)
        except:
            continue

        list_activities = df[' activity inference'].tolist()
        print len(list_activities)
        count_activity = collections.Counter(list_activities)

        most_freq = count_activity.most_common(1)
        temp_list.append(most_freq[0][0])

        average = (count_activity[1] + count_activity[2])/float(len(list_activities))
        temp_list.append(average)
        print count_activity
        #print count_activity[0]
        #raw_input()

        # for index, item in df.iterrows():
        #     list_activities.append(item[' activity inference'])
        with open("physical_activity.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(temp_list)
def phone_activity():
    counter = 0

    with open("phone_activity.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(['uid','mean_duration_dark','std_dark','mean_lock_duration','std_lock'])

    while counter<=60:
        counter+=1
        temp_list = []

        if counter < 10:
            user_id = 'u0' + str(counter)
        else:
            user_id = 'u' + str(counter)

        temp_list.append(user_id)


        try:
            df = pd.read_csv('StudentLife_AssignmentData/SensingData/PhoneLight/dark_' + user_id + '.csv',index_col=False)
        except:
            continue

        list_dark_duration = []
        for index,item in df.iterrows():
            list_dark_duration.append(item['end']-item['start'])
        temp_list.append(np.mean(list_dark_duration))
        temp_list.append(np.std(list_dark_duration))

        try:
            df = pd.read_csv('StudentLife_AssignmentData/SensingData/PhoneLock/phonelock_' + user_id + '.csv',index_col=False)
        except:
            continue

        list_lock_duration = []
        for index,item in df.iterrows():
            list_lock_duration.append(item['end']-item['start'])
        temp_list.append(np.mean(list_lock_duration))
        temp_list.append(np.std(list_lock_duration))

        with open("phone_activity.csv",'a') as f1:
            csvWriter = writer(f1)
            csvWriter.writerow(temp_list)

def regression(trainingFile):
    df_input=pd.read_csv(trainingFile,index_col=False)
    df_output = pd.read_csv("StudentLife_AssignmentData/GroundTruth/grades.csv",index_col=False)

    df_input = df_input.set_index('uid')
    df_output = df_output.set_index('uid')


    df_entire = pd.concat([df_input,df_output],axis=1,join='outer')

    df_entire = df_entire.fillna(value=0)
    print df_entire
    print df_entire.isnull().values.any()
    print df_entire.columns.values

    y= df_entire[' gpa all']
    list_columns_temp = (df_entire.columns.values)
    list_columns=[]
    for item in list_columns_temp:
        list_columns.append(item)

    list_columns.remove(' gpa 13s')
    list_columns.remove(' cs 65')
    list_columns.remove(' gpa all')

    df_X = df_entire[list_columns]
    print df_X
    import statsmodels.api as sm
    model = sm.OLS(y,df_X)
    results = model.fit()

    print (results.summary())


    # x = df_entire


if __name__ == '__main__':
    # mentalWellBeing()
    # socialEngagement()
    # mobility()
    # activity()
    # phone_activity()
    regression('output_mentalWellBeing.csv')