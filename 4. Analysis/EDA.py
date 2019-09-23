import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

df=pd.read_csv('../1. Original Data/churn_data.csv')

df.head(5)
df.columns()
df.describe()

#Cleaning Data
# Checkining Nans
# Remove nans from age columns (drop whole rows)
df = df[pd.notnull(df['age'])]
#Remove columns with too much nan (i.e. Credit Score,rewards earned )
df = df.drop(columns=['credit_score','rewards_earned'])

#Built histoggrams
# create traces
traces = [go.Scatter(
    x = df['cols']) for cols in df.columns]
