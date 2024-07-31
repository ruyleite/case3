pip install -r requirements.txt
#sudo apt-get install python-tk

cat vendas.csv > vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv
echo $'\n' >> vendas_grandes.csv
tail -n +2 vendas.csv >> vendas_grandes.csv


 ./monitora.sh cogna_pandas.py

 ./monitora.sh cogna_duckdb.py

 ./monitora.sh cogna_polars.py