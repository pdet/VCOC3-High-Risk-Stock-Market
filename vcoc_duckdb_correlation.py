#####################################################
# VCOC3 Lifestyle Research Team
# TEORIA DE PORTFOLIO (Markowitz)
# Objetivo: correlacao de ativos
# INPUT: datas de inicio, fim e tickers de ativos (portfolio)
# OUTPUT: Correlacao do portfolio e matriz 
#####################################################

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
from datetime import datetime
import duckdb

con = duckdb.connect('')

dt_ini=datetime(2013, 1, 1) 
dt_fim=datetime(2020, 1, 21) 

# RESUMO: reduzir ,'ITUB3.SA'
#tickers = ['XPML11.SA','RBRF11.SA','BBSE3.SA','TRPL4.SA','PETR4.SA','VVAR3.SA','BPAC3.SA','PSSA3.SA','ENBR3.SA','HYPE3.SA','WEGE3.SA','CPTS11B.SA','TUPY3.SA','HGLG11.SA','ITUB3.SA','MYPK3.SA','LREN3.SA','HGTX3.SA']
# atual
#tickers = ['ENBR3.SA','ABEV3.SA','PSSA3.SA','VVAR3.SA','TRPL4.SA','BPAC3.SA','TUPY3.SA','WEGE3.SA','HGTX3.SA','MYPK3.SA','LREN3.SA']

# Diego
#tickers = ['MYPK3.SA','CAML3.SA','SLCE3.SA','MOVI3.SA','COGN3.SA','TUPY3.SA','ITSA4.SA','PRIO3.SA','BBAS3.SA','LCAM3.SA','PTBL3.SA','MDIA3.SA','TAEE11.SA','HGTX3.SA','VVAR3.SA']


# atual tirando HGTX3 e MYPK3
tickers = ['ENBR3.SA','BBSE3.SA','PSSA3.SA','MRFG3.SA','TRPL4.SA','BPAC3.SA','XPML11.SA','RBRF11.SA','CPTS11B.SA','TUPY3.SA','LREN3.SA','WEGE3.SA','HGLG11.SA','ITUB3.SA','HYPE3.SA']#,'PETR4.SA','HGTX3.SA','MYPK3.SA']
# Menor correlacao, tira: BBSE3.SA 'ITUB3.SA','HYPE3.SA','HGTX3.SA','MYPK3.SA', 'LREN3.SA','PETR4.SA'
#tickers = ['ENBR3.SA','ABEV3.SA','PSSA3.SA','MRFG3.SA','TRPL4.SA','BPAC3.SA','XPML11.SA','RBRF11.SA','CPTS11B.SA','TUPY3.SA','WEGE3.SA','HGLG11.SA','VVAR3.SA']


# faz dowload dos precos ajustados diarios de fechamento 
# ERRO na incusão do dataframe no duckdb
bova=wb.DataReader(tickers, data_source='yahoo', start=dt_ini, end=dt_fim)['Adj Close']
bova.to_sql("bova", con, if_exists="replace")

# descobre a data na qual todos os tickers tem precos pra evitar problema de amostras diferentes na correlacao
# Correlacao deve ter o mesmo tamanho de amostra com precos dos ativos exatamente nos mesmos dias
valid_date = dt_ini
valid_tick =''
for tick in tickers:
	if !isNaN(data[tick].first_valid_index()):
		if data[tick].first_valid_index() > valid_date:
			valid_date=bova[tick].first_valid_index()
			valid_tick=tick

print ("Primeira bova valida: "+valid_date.strftime("%Y-%m-%d")+" ticker "+valid_tick)
print ("Intervalo de tempo da correlacao entre "+valid_date.strftime("%Y-%m-%d")+" e "+dt_fim.strftime("%Y-%m-%d"))

data.head()

#plt.plot(data)
#plt.legend(['BPAC11.SA', 'ENBR3.SA','BBSE3.SA','XPML11.SA','MYPK3.SA','WEGE3.SA','PSSA3.SA','LEVE3.SA','PETR4.SA','CAML3.SA','VVAR3.SA','ABEV3.SA','QUAL3.SA','HYPE3.SA','ITUB3.SA', 'LREN3.SA'],loc=2)

returns=pd.DataFrame()

# Normalizar os precos das acoes para encontrar a correlacao
for stock in tickers:
	if stock not in returns:
		returns[stock]=np.log(bova[stock]).diff()

returns.head()

# elimina a primeira linha com NaN  usando returns[1:]
# elimina datas com NaN pra fazer correlacao com .loc[valid_date.strftime("%Y-%m-%d"):'2019-12-12']
returns=returns[1:].loc[valid_date.strftime("%Y-%m-%d"):dt_fim.strftime("%Y-%m-%d")]

portfolio_corr=returns.corr().mean()

print("Media da correlacao do portfolio: ")
print(portfolio_corr.mean())

print("Correlacao do portfolio: ")
print(portfolio_corr)

print("Matriz de Correlacao do portfolio: ")
print(returns.corr())
