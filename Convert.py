import pandas as pd

print('\nConverting .CSV to .XLSX File...')

cont_1 = [1,2,3,4,5,6,7,8,9]
cont_2 = [10,11,12]

for i in cont_1:
    readfile = pd.read_csv(f'ETHUSDT-1h-2022-0{i}.csv')
    readfile.to_excel(f'ETHUSDT-1h-2022-0{i}.xlsx', index=None, header = True , startcol=0 , startrow=1)
    
for i in cont_2:
    readfile = pd.read_csv(f'ETHUSDT-1h-2022-{i}.csv')
    readfile.to_excel(f'ETHUSDT-1h-2022-{i}.xlsx', index=None, header = True , startcol=0 , startrow=1)

print('Formatting XLSX file...')

for i in cont_1:
    data = pd.read_excel(f'ETHUSDT-1h-2022-0{i}.xlsx')
    data.columns = ['date','open','high','low','close','F','G','H','I','J','K','L']
    data.set_index('date', inplace=True)
    data.drop(['F','G','H','I','J','K','L'],axis=1,inplace=True)
    data.index = pd.to_datetime(data.index, unit='ms')
    data.to_excel(f'ETHUSDT-1h-2022-0{i}.xlsx')

for i in cont_2:
    data = pd.read_excel(f'ETHUSDT-1h-2022-{i}.xlsx')
    data.columns = ['date','open','high','low','close','F','G','H','I','J','K','L']
    data.set_index('date', inplace=True)
    data.drop(['F','G','H','I','J','K','L'],axis=1,inplace=True)
    data.index = pd.to_datetime(data.index, unit='ms')
    data.to_excel(f'ETHUSDT-1h-2022-{i}.xlsx')

print('Concatenating...')

d1 = pd.read_excel('ETHUSDT-1h-2022-01.xlsx')
d2 = pd.read_excel('ETHUSDT-1h-2022-02.xlsx')
d3 = pd.read_excel('ETHUSDT-1h-2022-03.xlsx')
d4 = pd.read_excel('ETHUSDT-1h-2022-04.xlsx')
d5 = pd.read_excel('ETHUSDT-1h-2022-05.xlsx')
d6 = pd.read_excel('ETHUSDT-1h-2022-06.xlsx')
d7 = pd.read_excel('ETHUSDT-1h-2022-07.xlsx')
d8 = pd.read_excel('ETHUSDT-1h-2022-08.xlsx')
d9 = pd.read_excel('ETHUSDT-1h-2022-09.xlsx')
d10 = pd.read_excel('ETHUSDT-1h-2022-10.xlsx')
d11 = pd.read_excel('ETHUSDT-1h-2022-11.xlsx')
d12 = pd.read_excel('ETHUSDT-1h-2022-12.xlsx')
data = pd.concat([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12], ignore_index=True)

data.to_excel('2022.xlsx')
print('\nSuccess')