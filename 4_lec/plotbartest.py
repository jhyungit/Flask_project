import pandas as pd
import plotly.express as px

## 1
# df = pd.read_csv('race.csv')
# print(df)
# fig = px.bar(df, x = 'race', y = 'Male')
# fig.show()

# 2
# df = pd.read_csv('race.csv')
# df = pd.melt(df, id_vars=['race'], var_name= 'gender', value_name='value')
# fig = px.bar(df, x = 'race', y = 'value', color = 'gender',
#     barmode = 'group')
# fig.show()

# df = pd.read_csv('births.csv',header=None)
# my_df = df[df['year']>=2000]
# my_df = pd.melt(my_df, id_vars=['year'], var_name= 'gender', value_name='value')
# fig = px.bar(my_df, x = 'year', y = 'value', color = 'gender',
# barmode = 'group')
# fig.show()

## 3
# df = pd.read_csv('race.csv')
# df = pd.melt(df, id_vars=['race'], var_name= 'gender', value_name='value')
# fig = px.bar(df, x = 'race', y = 'value', color = 'gender',
#     barmode = 'group', facet_row = 'gender')
# fig.show()

# # 4
# df = pd.read_csv('race.csv')
# df = pd.melt(df, id_vars=['race'], var_name= 'gender', value_name='value')
# fig = px.bar(df, x = 'race', y = 'value', color = 'gender',
#     barmode = 'group', facet_col = 'gender')
# fig.show()