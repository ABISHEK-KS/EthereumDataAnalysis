import matplotlib.pyplot as plt 
import pandas as pd

import csv 
filedat=pd.read_csv("data_cleaned.csv")
listdates = list(filedat['Date'])
listcloseval=list(filedat['Close'])
trend1 =listdates[400:1012]
trend1val=listcloseval[400:1012]
plt.title('FIRST PEAK SCENARIO')
plt.xlabel('DATE')
plt.ylabel('CLOSING VALUE')
plt.plot(trend1,trend1val,'--')
plt.show()

trend2=listdates[1463:2380]
trend2val=listcloseval[1463:2380]
)
plt.title('SECOND PEAK SCENARIO')
plt.xlabel('DATE')
plt.ylabel('CLOSING VALUE')
plt.plot(trend2,trend2val,'--')
plt.show()
