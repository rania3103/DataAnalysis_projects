import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
# print(df.head())
# 2
BMI = df['weight'] / ((df['height'] / 100) ** 2)
df['BMI'] = BMI
df.drop(columns='BMI', inplace=True)
df['overweight'] = (BMI > 25).astype(int)
# print(df.head())
# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
# print(df)
# 4


def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=[
            'cholesterol',
            'gluc',
            'smoke',
            'alco',
            'active',
            'overweight'])
    # print(df_cat)

    # 6
    df_cat = df_cat.groupby(
        ['cardio', 'variable', 'value']).size().reset_index()
    # print(df_cat)
    df_cat.rename(columns={0: 'count'}, inplace=True)
    # print(df_cat)

    # # 7

    # # 8
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='count',
        hue='value',
        col='cardio',
        kind='bar')

    # # 9
    fig.savefig('catplot.png')
    return df_cat


# # 10
def draw_heat_map():
    #     # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

#     # 12
    corr = df_heat.corr()
#     # 13
    mask = np.triu(corr)


#     # 14
    fig, ax = plt.subplots()
#     # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True)

#     # 16
    fig.savefig('heatmap.png')
    return fig
