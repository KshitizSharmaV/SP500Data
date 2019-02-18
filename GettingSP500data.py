#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:15:02 2019

@author: kshitizsharma
"""

########################################
# Getting SP500 Data
########################################  
import datapackage
import pandas as pd
from datetime import datetime, timedelta
from iexfinance.stocks import get_historical_data
import pandas as pd


start = datetime.today()-timedelta(days=5*252)
#end = datetime(2010, 1, 1)
end=datetime.today()

def get_price_data_function(batch):
    df=get_historical_data(batch, start, end, output_format='pandas')
    return(df)
    
data_url = 'https://datahub.io/core/s-and-p-500-companies/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        data = pd.read_csv(resource.descriptor['path'])
        print (data)    

sp500tickers=list(data['Symbol'])
#list_to_remove=['CTL','FTV','MKC','SPGI','ZION']
#sp500tickers= list(set(sp500tickers).difference(set(list_to_remove)))


sp500data=get_price_data_function(sp500tickers[0:100])        
t=100
for i in range(100,len(sp500tickers),100):
    if(i<500):
        t=t+100
    else:
        t=len(sp500tickers)
    print(i)
    print(t)
    temp=get_price_data_function(sp500tickers[i:t])        
    sp500data=pd.concat([sp500data, temp],axis=1,sort=False)
    if(i==200):
        break

sp500dataclose=sp500data.xs('close',axis=1, level=1, drop_level=True)
sp500dataclose.to_csv('sp500closedata.csv',index=None,header=True)


########################################
# Getting SP500 Data
########################################   