import csv
import pandas as pd
import numpy as np

def mentalWellBeing():

	df_flourishing = pd.read_csv("Assignment_III/StudentLife_AssignmentData/Surveys/FlourishingScale.csv")
	df_loneliness = pd.read_csv("Assignment_III/StudentLife_AssignmentData/Surveys/LonelinessScale.csv")
	df_panas = pd.read_csv("Assignment_III/StudentLife_AssignmentData/Surveys/panas.csv")
	df_phq = pd.read_csv("Assignment_III/StudentLife_AssignmentData/Surveys/PHQ-9.csv")
	df_perceivedStress = pd.read_csv("Assignment_III/StudentLife_AssignmentData/Surveys/PerceivedStressScale.csv")


	print df_flourishing
	print df_phq


if __name__ == '__main__':
	mentalWellBeing()