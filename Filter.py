import pandas as pd
from datetime import datetime

data = pd.read_excel('2022.xlsx',index_col=0, parse_dates=True)

cantDatos = len(data.index)
cantDatos = int(cantDatos)
#data.set_index(data['date'][1])
print('\ncantDatos: ', cantDatos)

data['change'] = 0.0
for i in range(0,cantDatos,1):
    hour = str(data['date'][i])
    if (hour == '00:00:00' or hour == '01:00:00' or hour == '02:00:00' or hour == '03:00:00' or hour == '04:00:00' or hour == '05:00:00' or hour == '06:00:00' or hour == '07:00:00' or hour == '08:00:00'):
        data['change'][i] = 1

data = data.loc[data['change'] != 0] 

print('\nSuccess\n')

data.to_excel('2022.xlsx')