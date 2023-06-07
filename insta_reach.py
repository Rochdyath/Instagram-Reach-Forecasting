import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("Instagram-Reach.csv", encoding = 'latin-1')
data['Date'] = pd.to_datetime(data['Date'])
print(data.head())