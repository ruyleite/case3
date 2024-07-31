#!/usr/bin/env python3
import pandas as pd
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%m/%d/%Y')

pd.set_option('display.float_format', str)

#Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
columns = ['region','country','item_type','sales_channel','order_priority','order_date','order_id','ship_date',
           'units_sold','unit_price','unit_cost','total_revenue','total_cost','total_profit']

#Criar um dataframe somente com as colunas a serem trabalhadas.
#Usar o parametro low_memory para reduzir a quantidade memoria durante a leitura.
#df = pd.read_csv("vendas.csv", names=columns, usecols=['item_type', 'sales_channel', 'units_sold'], header=1, sep=',', low_memory=True)
#Quebrando a leitura do arquivo em flagmentos.
df_chunk = pd.read_csv("vendas_grandes.csv", names=columns,
                       usecols=['region','country','item_type', 'sales_channel', 'order_date', 'units_sold','total_revenue'],
                       header=1, sep=',', low_memory=True, chunksize=1000000,
                       parse_dates=['order_date'], date_parser=dateparse)

array_df = []

for chunk in df_chunk:
    array_df.append(chunk.groupby(['region', 'country', 'item_type', 'sales_channel', 'order_date']).sum())

df = pd.concat(array_df, ignore_index=False)
df = df.reset_index()

print('Produtos mais vendidos por canal')
print(df[['sales_channel', 'item_type', 'units_sold']].groupby(['sales_channel', 'item_type']).sum().sort_values(['sales_channel', 'units_sold'], ascending=False))

#print('Produtos mais vendidos')
#print(df[['item_type', 'units_sold']].groupby(['item_type']).sum().sort_values(['item_type', 'units_sold']))

pd.set_option('display.float_format', lambda x: '%10d' % x)
print('Pais e região teve o maior volume de vendas (em valor)')
print(df[['region', 'country', 'total_revenue']].groupby(['region', 'country']).sum().sort_values(['total_revenue'], ascending=False))

print('Média de vendas mensais por produto')
df['ano_mes'] = pd.to_datetime(df.order_date, format='%Y-%m')
df = df[['item_type', 'ano_mes', 'total_revenue']].groupby(['item_type', 'ano_mes']).sum().reset_index()
print(df[['item_type', 'total_revenue']].groupby(['item_type']).median().sort_values(['total_revenue']))