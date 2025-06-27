import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller,kpss
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import SimpleExpSmoothing,Holt,ExponentialSmoothing

df=pd.read_csv('Amazon.csv')
"""df.index=pd.date_range(start='2004-01-02',periods=len(df),freq='B')
df.index.name='Date'
df['rt'].plot(title='Amzon Daily Log Returns',figsize=(10,4))
plt.ylabel('Log Return')
plt.savefig('TSA.png')"""

#convert log returns to synthetic price
df['Price']=100*(1+df['rt']).cumprod()
"""df['Price'].plot(title='Reconstructed AMZN Price',figsize=(10,5))
plt.ylabel("Price")
plt.grid(True)
plt.savefig('TSA.png')"""

#adf and rolling stats
roll_mean=df['Price'].rolling(window=30).mean()
roll_std=df['Price'].rolling(window=30).std()
"""plt.plot(df['Price'],label="Original")
plt.plot(roll_mean,label='Rolling Mean')
plt.plot(roll_std,label='Rolling Std')
plt.title('Rolling Mean & Standard Deviation')
plt.legend()
plt.grid(True)
plt.savefig('TSA.png')"""

#adf test
result=adfuller(df['Price'])
"""print("ADF Statistic:",result[0])
print("p-value:",result[1])
if result[1]<0.05:
    print("Stationary")
else:
    print("Not Stationary")"""

#first order differencing:
df['Price_diff']=df['Price'].diff()
"""df['Price_diff'].dropna().plot(title="First-Order Differenced Price",figsize=(10,4))
plt.grid(True)
plt.savefig('TSA.png')
result=adfuller(df['Price_diff'].dropna())
print("Differenced ADF p-value:",result[1])"""

#ACF and PACF plots
"""plot_acf(df['Price_diff'].dropna(),lags=40)
plt.title("ACF Plot")
plt.savefig("ACF.png")
plot_pacf(df['Price_diff'].dropna(),lags=40)
plt.title("PACF Plot")
plt.savefig("PACF.png")"""

#ARIMA Model
"""model=ARIMA(df['Price'],order=(1,1,1))
model_fit=model.fit()
print(model_fit.summary())
forecast=model_fit.forecast(steps=10)
print("Forecast",forecast)"""

#Simple Exponenential Smoothing
"""ses_model=SimpleExpSmoothing(df['Price']).fit(smoothing_level=0.2,optimized=False)
ses_forecast=ses_model.forecast(12)
df['Price'].plot(label='Original', figsize=(10, 5))
ses_model.fittedvalues.plot(label='SES Fit')
ses_forecast.plot(label='SES Forecast')
plt.legend()
plt.savefig('SES.png')"""

#Holts linear trend:
"""holt_model = Holt(df['Price']).fit()
holt_forecast = holt_model.forecast(12)

df['Price'].plot(label='Original')
holt_model.fittedvalues.plot(label='Holt Fit')
holt_forecast.plot(label='Holt Forecast')
plt.legend()
plt.title("Holt's Linear Trend Model")
plt.savefig("Holts.png")"""

#Holts winters
"""hw_model = ExponentialSmoothing(df['Price'], trend='add', seasonal='add', seasonal_periods=252).fit()
hw_forecast = hw_model.forecast(12)

df['Price'].plot(label='Original')
hw_model.fittedvalues.plot(label='HW Fit')
hw_forecast.plot(label='HW Forecast')
plt.legend()
plt.title("Holt-Winters Model")
plt.savefig("holts_winters.png")"""

#MACS:Moving average crossover strategy
df['SMA_20'] = df['Price'].rolling(window=20).mean()
df['SMA_50'] = df['Price'].rolling(window=50).mean()
plt.figure(figsize=(12, 6))
plt.plot(df['Price'], label='Price')
plt.plot(df['SMA_20'], label='20-Day SMA')
plt.plot(df['SMA_50'], label='50-Day SMA')
plt.title("Moving Average Crossover Strategy")
plt.legend()
plt.grid(True)
plt.savefig("MACS.png")
