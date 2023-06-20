import pandas as pd
from prophet import Prophet

dataframe = pd.read_csv('http://61.247.189.150/arafat-anwar/sales/transactions.csv')
dataframe.head()

dataframe.dtypes

dataframe ['date'] = pd.to_datetime(dataframe ['date'])
dataframe.dtypes

dataframe.drop('store_nbr', axis=1, inplace=True)

dataframe.columns = ['ds', 'y']
dataframe.head()

p = Prophet(interval_width=0.92, daily_seasonality=True)

model = p.fit(dataframe)

future = p.make_future_dataframe(periods=200, freq='D')
future.tail()

forecast_prediction = p.predict(future)
forecast_prediction.tail()

plot1 = p.plot(forecast_prediction)
plot2 = p.plot_components(forecast_prediction)