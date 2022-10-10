import pandas as pd
import numpy as np


def filter_extreme_MAD(dataframe,n=3):
    # MAD:绝对中位差去极值
    for i in dataframe.columns:
        median = dataframe[i].quantile(0.5)
        new_median = ((dataframe[i] - median).abs()).quantile(0.50)
        max_range = median + n * new_median
        min_range = median - n * new_median
        dataframe[i]=pd.DataFrame(np.clip(dataframe[i].values, min_range, max_range),columns=None)

    return dataframe
def filter_extreme_3sigma(dataframe,n=3):
    # 3sigma 去极值
    for i in dataframe.columns:
        mean=dataframe[i].mean()
        std=dataframe[i].std()
        max_range=mean+n*std
        min_range=mean-n*std
        dataframe[i] = pd.DataFrame(np.clip(dataframe[i].values, min_range, max_range), columns=None)
    return dataframe

def filter_extreme_percentile(dataframe,min=0.025,max=0.975):
    # 百分位法 去极值
    for i in dataframe.columns:
        Temp=dataframe[i].sort_values()
        q=Temp.quantile([min,max])
        dataframe[i] = pd.DataFrame(np.clip(dataframe[i].values, q.iloc[0], q.iloc[1]), columns=None)
    return dataframe