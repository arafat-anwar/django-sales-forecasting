from django.shortcuts import render
import pandas as pd
from prophet import Prophet
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import io
import urllib
from django.http import HttpResponse

def index(request):
	predicted = 0
	if request.method == "POST":
		path = request.POST.get("path", "")
		periods = request.POST.get("periods", "")
		dataframe = pd.read_csv(path)
		dataframe.head()

		dataframe.dtypes

		dataframe ['date'] = pd.to_datetime(dataframe ['date'])
		dataframe.dtypes

		dataframe.drop('store_nbr', axis=1, inplace=True)

		dataframe.columns = ['ds', 'y']
		dataframe.head()

		p = Prophet(interval_width=0.92, daily_seasonality=True)

		model = p.fit(dataframe)

		future = p.make_future_dataframe(periods=int(periods), freq='D')
		future.tail()

		forecast_prediction = p.predict(future)
		forecast_prediction.tail()

		plot1 = p.plot(forecast_prediction)
		plot1.savefig('myapp/static/plot.png')

		plot2 = p.plot_components(forecast_prediction)
		plot2.savefig('myapp/static/plot_components.png')

		predicted = 1
	
	context = {
		"predicted": predicted,
	}

	return render(request, "index.html", context)
