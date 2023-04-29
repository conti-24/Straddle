import pandas as pd

data = pd.read_excel('ETHUSDT-1h-2023-01.xlsx',index_col=0, parse_dates=True)
cantDatos = data.index_size
cantDatos = int(cantDatos)

