import plotly.express as px
import pandas as pd
df = pd.read_csv('DataPr100.csv')
fig = px.scatter(df,x='Date',y="Cases",color="Country",title="Covid Cases of 2020")
fig.show()