#!/usr/bin/env python3
import polars as pl
from datetime import datetime

columns = ['region','country','item_type','sales_channel','order_priority','order_date','order_id','ship_date',
           'units_sold','unit_price','unit_cost','total_revenue','total_cost','total_profit']

df = pl.read_csv("vendas_grandes.csv", has_header=True, separator=',', new_columns=columns)

print('Produtos mais vendidos por canal')
print(df.select(["sales_channel", "item_type", 'units_sold']).group_by(["sales_channel", "item_type"]).sum().sort("sales_channel", 'units_sold', descending=[False, True]))

#print('Produtos mais vendidos')
#print(df.select(["item_type", 'units_sold']).group_by("item_type").sum().sort("units_sold", descending=True))


print('Pais e região teve o maior volume de vendas (em valor)')
print(df.select(['region', 'country', 'total_revenue']).group_by('region', 'country').sum().sort("total_revenue", descending=True))


print('Média de vendas mensais por produto')
df = df.with_columns(pl.col("order_date").str.to_datetime("%m/%d/%Y"))
df = df.with_columns(pl.col("order_date").dt.strftime('%Y%m').cast(pl.Int32).alias('ano_mes'))
df = df.select(['item_type', 'ano_mes', 'total_revenue']).group_by(['item_type', 'ano_mes']).sum()

print(df.select(['item_type', 'total_revenue']).group_by('item_type').median().sort("total_revenue").with_columns(pl.selectors.float().map_elements('{:.2f}'.format)))
