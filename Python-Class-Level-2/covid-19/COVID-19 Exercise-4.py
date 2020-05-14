import pandas as pd

covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv')
c_data = covid_data[covid_data['Country_Region']=='Australia']
c_data['Active'] = c_data['Confirmed'] - c_data['Deaths'] - c_data['Recovered']
c_data = c_data[['Province_State', 'Confirmed', 'Deaths', 'Recovered','Active']]
result = c_data.sort_values(by='Confirmed', ascending=False)
result = result.reset_index()
print(result)
