import pandas as pd

data = pd.read_excel('2022.xlsx',index_col=0, parse_dates=True)
cantDatos = len(data.index)
cantDatos = int(cantDatos)
#data.set_index(data['date'][0])

data['change'] = 0.0
'''
for i in range(0,cantDatos,1):
    hour = str(data['date'][i])
    if (hour == '00:00:00' or hour == '01:00:00' or hour == '02:00:00' or hour == '03:00:00' or hour == '04:00:00' or hour == '05:00:00' or hour == '06:00:00' or hour == '07:00:00' or hour == '08:00:00'):
        data['change'][i] = 1

data = data.loc[data['change'] != 0] 
'''



'''
data['call_strike'] = 0.0
data['put_strike'] = 0.0
data['premium'] = 0.0
data['cont'] = 0.0
data['roe'] = 0.0
data['pnl'] = 0.0
data['capital'] = 0.0
data['withdrawn'] = 0.0

callBE = 0.01
putBE = 0.99
premium = 0.003
stop = 0.02
cont = 0 
maxCont = 500
withdrawn = 0.0
capi = 100
capital = capi
it = 30
target = 50
winners = 0
losers = 0
total = winners + losers


for i in range(0,cantDatos,1):
    data['change'][i] = (((data['close'][i] / data['open'][i] ) -1 ) *100 )
    data['call_strike'][i] = data['open'][i] * (1 + callBE)
    data['put_strike'][i] = data['open'][i] * putBE
    data['premium'][i] = (data['open'][i] * premium)
    cont = ((capital * stop) / data['premium'][i])

    if (cont > maxCont):
        data['cont'][i] = maxCont
    else:
        data['cont'][i] = cont

    if (data['close'][i] > data['call_strike'][i]):
        data['roe'][i] = ((data['close'][i] - data['call_strike'][i] ) / data['premium'][i])
    elif (data['close'][i] < data['put_strike'][i]):
        data['roe'][i] = ((data['put_strike'][i] - data['close'][i] / data['premium'][i]))
    elif (data['close'][i] <= data['call_strike'][i] and data['close'][i] >= data['put_strike'][i]):
        data['roe'][i] = 0

    profit = ( data['roe'][i] * data['premium'][i] * data['cont'][i] )
    loss = data['premium'][i] * data['cont'][i]

    if (data['roe'][i] == 0):
        capital -= loss
        data['pnl'][i] = loss
    else:
        capital += profit
        data['pnl'][i] = profit
        data['capital'][i] = capital

print('Winners: ', winners)
print('Losers: ', losers)
'''
print('success')

data.to_excel('2022.xlsx')

'''
# Withdrawn Settings at Withdrawal

    if (capital > capi):
        if ((capital * 0.2) >= 100):
            withdrawn += ((capital - capi) * 0.8 )
            capi = capital * 0.2
            capital = capi
        else:
            withdrawn = withdrawn + (capital *0.8) - (100 - (capital * (0.2) ) )
            capi = 100
            capita = capi
    elif (capital <= capi):
        withdrawn -= (capi - capital)
        capi = 100
        capital = capi
    data['withdrawn'][j] = withdrawn
'''

