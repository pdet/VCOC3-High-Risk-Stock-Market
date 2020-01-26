#####################################################
# VCOC3 Lifestyle Research Team
# TEORIA DE PORTFOLIO (Markowitz)
# Aulas: https://ocw.mit.edu/courses/sloan-school-of-management/15-401-finance-theory-i-fall-2008/video-lectures-and-slides/portfolio-theory/
# https://www.youtube.com/watch?v=Nu4lHaSh7D4
# Fontes do codigo gosmento
# https://github.com/PyDataBlog/Python-for-Data-Science/tree/master/Tutorials
# https://medium.com/python-data/efficient-frontier-portfolio-optimization-with-python-part-2-2-2fe23413ad94
# https://towardsdatascience.com/stock-analysis-in-python-a0054e2c1a4c
#######################################
#import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
import random

# get adjusted closing prices of 5 selected companies with Quandl
# quandl.ApiConfig.api_key = 'PASTE YOUR API KEY HERE'
# CARTEIRA: empiricus
# tickers = ['CPFE3.SA','ALUP11.SA','BBAS3.SA','CNTO3.SA','CSAN3.SA','CVCB3.SA','BPAN4.SA','JPSA3.SA','GNDI3.SA','LREN3.SA','VVAR3.SA','AZUL4.SA','BPAC11.SA','GOAU4.SA','MGLU3.SA','PRIO3.SA','RAPT4.SA']

# Andre
#tickers = ['WEGE3.SA','NEOE3.SA','KLBN3.SA','SUZB3.SA','STBP3.SA','COGN3.SA','PTBL3.SA','VVAR3.SA','ITSA4.SA','PETR4.SA','VALE3.SA','BPAC11.SA', 'ITUB3.SA', 'ENBR3.SA', 'LREN3.SA','BBSE3.SA','XPML11.SA','MYPK3.SA','PSSA3.SA','LEVE3.SA','UGPA3.SA','ALUP11.SA','GNDI3.SA','ROMI3.SA','SLCE3.SA','MOVI3.SA','CPFE3.SA','BBAS3.SA','CNTO3.SA','CSAN3.SA','CVCB3.SA','BPAN4.SA','JPSA3.SA','MGLU3.SA','PRIO3.SA','RAPT4.SA','CAML3.SA','HGTX3.SA','POMO4.SA']

# CARTEIRA: microcap alert
# tickers = ['CAML3.SA','MOVI3.SA','ROMI3.SA','HGTX3.SA','SLCE3.SA','POMO4.SA','SQIA3.SA','LPSB3.SA','AALR3.SA','OFSA3.SA','SHOW3.SA','LOGG3.SA','JPSA3.SA','CCPR3.SA']
# tickers = ['CAML3.SA','MOVI3.SA','ROMI3.SA','HGTX3.SA','SLCE3.SA','POMO4.SA']

# CARTEIRA: oportunidade de uma vida
# tickers = ['RLOG3.SA','SAPR11.SA','ENEV3.SA','BPAC11.SA','JPSA3.SA','PETR4.SA','OIBR3.SA','CNTO3.SA','BPAN4.SA','MGLU3.SA','VVAR3.SA','AZUL4.SA','CSNA3.SA','ALSO3.SA']
# tickers = ['SAPR11.SA','BPAC11.SA','CNTO3.SA','MGLU3.SA']


#tickers = ['BPAC11.SA', 'ITUB3.SA', 'ENBR3.SA', 'LREN3.SA','BBSE3.SA','XPML11.SA','MYPK3.SA','WEGE3.SA','PSSA3.SA','UGPA3.SA',
#'LCAM3.SA','HYPE3.SA','PETR4.SA','CAML3.SA','ROMI3.SA','VVAR3.SA','TRPL4.SA','ABEV3.SA','QUAL3.SA']
# tickers = ['BPAC11.SA', 'ITUB3.SA', 'ENBR3.SA', 'LREN3.SA','PSSA3.SA','XPML11.SA','HYPE3.SA','MYPK3.SA','WEGE3.SA','PETR4.SA','VVAR3.SA']
#tickers = ['BPAC11.SA', 'ENBR3.SA','BBSE3.SA','XPML11.SA','MYPK3.SA','WEGE3.SA','PSSA3.SA','LEVE3.SA','PETR4.SA','CAML3.SA','VVAR3.SA','ABEV3.SA','QUAL3.SA','HYPE3.SA','ITUB3.SA', 'LREN3.SA']
#tickers = ['ENBR3.SA','BBSE3.SA','MYPK3.SA','WEGE3.SA','PSSA3.SA','PETR4.SA','VVAR3.SA','HYPE3.SA','LREN3.SA','TRPL4.SA','BPAC3.SA','XPML11.SA','RBRF11.SA','CPTS11B.SA','TUPY3.SA']
tickers = ['ENBR3.SA','BBSE3.SA','PSSA3.SA','VVAR3.SA','HYPE3.SA','TRPL4.SA','BPAC3.SA','XPML11.SA','RBRF11.SA','CPTS11B.SA','TUPY3.SA','LREN3.SA','HGTX3.SA','MYPK3.SA','WEGE3.SA']


# melhores das simulacoes
#tickers = ['BPAC11.SA', 'ENBR3.SA', 'LREN3.SA','MYPK3.SA','WEGE3.SA','PSSA3.SA','VVAR3.SA','LEVE3.SA','UGPA3.SA','ROMI3.SA','SLCE3.SA','ALUP11.SA']


# Define a quantidade de acoes do portfolio (meu numero magico eh 12, pq so consigo acompanhar o balanco de 12 empresas)
PORTFOLIO_SIZE=15
if len(tickers) < 10:
    PORTFOLIO_SIZE=len(tickers)

# Define o numero de carteiras aleatorios sobre a lista de tickers
NUM_CARTEIRAS=1

# data = quandl.get_table('WIKI/PRICES', ticker = selected,
#                        qopts = { 'columns': ['date', 'ticker', 'adj_close'] },
#                        date = { 'gte': '2014-1-1', 'lte': '2016-12-31' }, paginate=True)


######################################
# Funcao que carrega os valores dos tickers
# INPUT: lista de tickers
# OUTPUT: lista com valor do fechamento na data 
######################################
#def carrega(tickers):
#    table=pd.DataFrame()
#    ignore_index=False
#    for t in tickers:
#        table[t]=wb.DataReader(t, data_source='yahoo', start='2010-1-1', end='2019-12-30')['Adj Close']
#    return table;
#def carrega(tickers):
#    table=pd.DataFrame()
#    table=wb.DataReader(tickers, data_source='yahoo', start='2010-1-1', end='2019-12-30')['Adj Close']
#    return table;


######################################
# Funcao que implementa a fronteira eficiente do Markowitz com 5000 tentativas de pesos
# INPUT: cotacoes dos tickers e nomes dos tickers
# OUTPUT: portfolio com pesos de maior retorno esperado 
######################################
def frontier(table):
    '''table=pd.DataFrame()
    ignore_index=False
    # tickers = [TickerA, TickerB, TickerC]

    for t in selected:
        table[t]=wb.DataReader(t, data_source='yahoo', start='2010-1-1', end='2019-12-22')['Adj Close']

    table.head()'''
    
    # reorganise data pulled by setting date as index with
    # columns of tickers and their corresponding adjusted prices
    # clean = data.set_index('date')
    # table = clean.pivot(columns='ticker')

    # lista de acoes pro portfolio escolhido
    selected = list(table.columns.values)

    # calculate daily and annual returns of the stocks
    returns_daily = table.pct_change()
    returns_annual = returns_daily.mean() * 250

    # get daily and covariance of returns of the stock
    cov_daily = returns_daily.cov()
    cov_annual = cov_daily * 250

    # empty lists to store returns, volatility and weights of imiginary portfolios
    port_returns = []
    port_volatility = []
    sharpe_ratio = []
    stock_weights = []

    # set the number of combinations for imaginary portfolios
    num_assets = len(selected)
    num_portfolios = 150000

    #set random seed for reproduction's sake
    np.random.seed(101)

    # populate the empty lists with each portfolios returns,risk and weights
    for single_portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        returns = np.dot(weights, returns_annual)
        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
        sharpe = returns / volatility
        sharpe_ratio.append(sharpe)
        port_returns.append(returns)
        port_volatility.append(volatility)
        stock_weights.append(weights)

    # a dictionary for Returns and Risk values of each portfolio
    portfolio = {'Returns': port_returns,
                 'Volatility': port_volatility,
                 'Sharpe Ratio': sharpe_ratio}

    # extend original dictionary to accomodate each ticker and weight in the portfolio
    for counter,symbol in enumerate(selected):
        portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]

    # make a nice dataframe of the extended dictionary
    df = pd.DataFrame(portfolio)

    # get better labels for desired arrangement of columns
    column_order = ['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' Weight' for stock in selected]

    # reorder dataframe columns
    df = df[column_order]

    # plot frontier, max sharpe & min Volatility values with a scatterplot
    '''plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Returns')
    plt.title('Efficient Frontier')
    plt.show()'''


    # find min Volatility & max sharpe values in the dataframe (df)
    min_volatility = df['Volatility'].min()
    max_sharpe = df['Sharpe Ratio'].max()

    # use the min, max values to locate and create the two special portfolios
    sharpe_portfolio = df.loc[df['Sharpe Ratio'] == max_sharpe]
    min_variance_port = df.loc[df['Volatility'] == min_volatility]

    # plot frontier, max sharpe & min Volatility values with a scatterplot
    '''plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'], c='red', marker='D', s=200)
    plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'], c='blue', marker='D', s=200 )
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Returns')
    plt.title('Efficient Frontier')
    plt.show()'''
    print(min_variance_port.T)
    print(sharpe_portfolio.T)
    # print(sharpe_portfolio['Returns'].max())
    return sharpe_portfolio,df;


######################################
# Funcao que aleatoriza uma carteira com base na lista de tickers
# INPUT: lista de tickers
# OUTPUT: lista aleatorio de tickers
######################################
def random_portfolio(selected):
    r_portfolio=range(PORTFOLIO_SIZE)
    random.shuffle(selected)
    for i in range(0,PORTFOLIO_SIZE):
        r_portfolio[i] = selected[i]
    return r_portfolio;

######################################
# Funcao pra plotar o melhor portfolio
# INPUT: dataframe
# OUTPUT: grafico com as estimativas e os melhores portfolios: min_variance e sharpe
######################################
def plota_portfolio(df):
    min_volatility = df['Volatility'].min()
    max_sharpe = df['Sharpe Ratio'].max()
    sharpe_portfolio = df.loc[df['Sharpe Ratio'] == max_sharpe]
    min_variance_port = df.loc[df['Volatility'] == min_volatility]
    plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'], c='red', marker='D', s=200)
    plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'], c='blue', marker='D', s=200 )
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Returns')
    plt.title('Efficient Frontier')
    plt.show()   


######################################
# Codigo principal
# TODO: repeat until predicted_portforlio_final > 1.8
######################################
table=pd.DataFrame()
# table = carrega(tickers)
table=wb.DataReader(tickers, data_source='yahoo', start='2017-12-28', end='2019-12-30')['Adj Close']
print(table.iloc[0])

porforlio_return_final = 0
for i in range(0,NUM_CARTEIRAS):
    r_portfolio = random_portfolio(tickers);
    new_table = table[r_portfolio]
    predicted_portforlio,df = frontier(new_table)
    print(r_portfolio)
    print(predicted_portforlio['Returns'].max())
    if porforlio_return_final < predicted_portforlio['Returns'].max():
        porforlio_return_final = predicted_portforlio['Returns'].max()
        final_portfolio = predicted_portforlio
        df_final=df
     

print('FINAL')
print(final_portfolio.T)
print(final_portfolio['Returns'].max())
plota_portfolio(df_final)



