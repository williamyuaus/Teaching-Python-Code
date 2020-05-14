import pandas as pd
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-16-2020.csv')
data = covid_data.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Recovered']==0][['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
pd.set_option('display.max_rows', None)
print(result)
