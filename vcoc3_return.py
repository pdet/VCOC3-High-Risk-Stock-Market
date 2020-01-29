#####################################################
# VCOC3 Lifestyle Research Team
# Retorno de uma carteira VCOC3 contra o Ibov
# TODO: incluir carteira teorica de Markowitz e fundos quantitativos
# Link fundos: http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/
#######################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
from datetime import datetime

dt_ini=datetime(2017, 01, 27) 
dt_fim=datetime(2020, 01, 27) 

#  Assets to be included in the portfolio
tickers = ['XPML11.SA','RBRF11.SA','BBSE3.SA','TRPL4.SA','MYPK3.SA','ITUB3.SA','LREN3.SA','PETR4.SA','VVAR3.SA','BPAC3.SA','PSSA3.SA',
'ENBR3.SA','HYPE3.SA','WEGE3.SA','CPTS11B.SA','TUPY3.SA','HGTX3.SA']

# Asset weights carteira atual e carteira teorica gerada pelo script de fronteira eficiente
wts = [0.26,0.026,0.05,0.046,0.033,0.081,0.046,0.039,0.04,0.053,0.13,0.046,0.023,0.027,0.029,0.017,0.019]
wts_theo = [0.13,0.057,0.082,0.155,0.013,0.016,0.03,0.009,0.004,0.15,0.092,0.003,0.0029,0.06,0.019,0.10,0.046]

# Serie Double Income da Empiricus
tickers_emp = ['ALUP11.SA','ABEV3.SA','BBSE3.SA','BRSR6.SA','ENBR3.SA','HGTX3.SA','HYPE3.SA','ITUB4.SA','QUAL3.SA','SAPR11.SA','VIVT4.SA',
'HGLG11.SA','KNCR11.SA','KNRI11.SA','XPML11.SA']
#wts_emp = [0.027,0.027,0.027,0.027,0.027,0.027,0.027,0.027,0.027,0.027,0.027,0.05,0.05,0.05,0.05]
wts_emp = [0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.11,0.11,0.11,0.11]

# Serie Portfolio Empiricus
tickers_emp2 = ['RBRR11.SA','VISC11.SA','HGLG11.SA','RBRF11.SA','BPAC3.SA','VIVT4.SA','MGLU3.SA','CSAN3.SA','CPFE3.SA','RAIL3.SA',
'PETR4.SA','SMAL11.SA']
#wts_emp2 = [0.025,0.033,0.025,0.04,0.025,0.025,0.025,0.025,0.05,0.05,0.05,0.05]
wts_emp2 = [0.055,0.073,0.055,0.088,0.055,0.055,0.055,0.055,0.11,0.11,0.11,0.11]

def cumul_ret(tickers,wts):
      price_data = web.get_data_yahoo(tickers,
                               start = dt_ini,
                               end = dt_fim)

      price_data = price_data['Adj Close']
      ret_data = price_data.pct_change()[1:]
      if wts is None:
            cumulative_ret = (ret_data + 1).cumprod()
      else:
            weighted_returns = (wts * ret_data)
            port_ret = weighted_returns.sum(axis=1)  
            cumulative_ret = (port_ret + 1).cumprod()

      return cumulative_ret;

# Juntando as series num unico dataframe
x1 = pd.Series(cumul_ret(tickers,wts))
x2 = pd.Series(cumul_ret('^BVSP',None))
x3 = pd.Series(cumul_ret(tickers,wts_theo))
x4 = pd.Series(cumul_ret(tickers_emp,wts_emp))
x5 = pd.Series(cumul_ret(tickers_emp2,wts_emp2))


cumulative = x1.to_frame(name="VCOC")
cumulative = cumulative.join(x2.to_frame(name="BVSP"))
cumulative = cumulative.join(x3.to_frame(name="Teorica"))
cumulative = cumulative.join(x4.to_frame(name="Double Income"))
cumulative = cumulative.join(x5.to_frame(name="Portfolio Empiricus"))


cumulative.columns=['VCOC','BVSP','Teorica','Double Income','Portfolio Empiricus']
cumulative.plot()

plt.show()
