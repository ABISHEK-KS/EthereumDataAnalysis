import csv

import pandas as pd
import pandas_profiling as pp

filedata=pd.read_csv("data_cleaned.csv")
profrep=pp.ProfileReport(filedata,title='ETHEREUM HISTORICAL DATA PROFILING (K.S.ABISHEK)')
profrep.to_file("ProfileReport.html")
