#!/usr/bin/env python3
import duckdb

#Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit

conn = duckdb.connect()
conn.execute("CREATE TABLE vendas AS SELECT * FROM read_csv_auto('vendas_grandes.csv')")
result = conn.execute('SELECT '
                      '       "Sales Channel" as sales_channel, '
                      '       "Item Type" as item_type, '                      
                      '       sum("Units Sold") as total_sales '
                      'FROM vendas '
                      'GROUP BY "Sales Channel", "Item Type" '
                      'order by sales_channel, total_sales desc').fetchall()
print('Produtos mais vendidos por canal')
print("sales_channel".rjust(20, ' '), "item_type".rjust(20, ' '), "total_sales")
for i in result:
    print(i[0].rjust(20, ' '), i[1].rjust(20, ' '), i[2])

#result = conn.execute('SELECT '
#                      '       "Item Type" as item_type, '
#                      '       sum("Units Sold") as total_sales '
#                      'FROM vendas '
#                      'GROUP BY "Item Type" '
#                      'order by total_sales desc').fetchall()

#print('Produtos mais vendidos')
#print("item_type".rjust(20, ' '), "total_sales")
#for i in result:
#    print(i[0].rjust(20, ' '), i[1])

print('Pais e região teve o maior volume de vendas (em valor)')
result = conn.execute('SELECT '
                      '       "Region" as region, '
                      '       "Country" as country,'
                      '       sum("Total Revenue") as total_revenue '
                      'FROM vendas '
                      'GROUP BY '
                      '       "Region", '
                      '       "Country" '
                      'order by total_revenue desc').fetchall()

print("Region".rjust(30, ' '), "Country".rjust(20, ' '), "total_revenue")
for i in result:
    print(i[0].rjust(30, ' '), i[1].rjust(30, ' '), i[2])


print('Média de vendas mensais por produto')

result = conn.execute('with base as'
                      '( SELECT '
                      '       "Item Type" as item_type, '
                      '       strftime("Order Date", \'%Y-%m\') as ano_mes,'
                      '       sum("Total Revenue") as total_revenue '
                      '  FROM vendas '
                      '  GROUP BY '
                      '       "Item Type", '
                      '       strftime("Order Date", \'%Y-%m\') '
                      ')'
                      'select item_type, avg(total_revenue) '
                      'from base '
                      'group by item_type').fetchall()

print("item_type".rjust(20, ' '), "media_mes")
for i in result:
    print(i[0].rjust(20, ' '), i[1])
