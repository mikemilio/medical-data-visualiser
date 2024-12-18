import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df[['weight', 'height']].apply(
    lambda x: 1 if x[0] / ( (x[1] / 100) ** 2 ) > 25 else 0, 
    axis=1)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1 )
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1 )

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(
        ['cardio', 'variable', 'value']).size().reset_index(name='count').rename(columns={'count': 'total'})
    

    # 7



    # 8
    fig = sns.catplot(data=df_cat, x='variable', y='total', 
                      hue='value', col='cardio', 
                      kind='bar', height=4, aspect=1.5)


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
