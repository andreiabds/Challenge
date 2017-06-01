import pandas as pd
import numpy as np

def series_cleaner(column_series):
    '''
    Returns a series with clean data.
    '''
    clean_series = column_series.str.strip().str.lower()

    #removing bad strings
    mask = np.logical_not(clean_series.isin(['', 'null', 'none', '0']))
    masked = clean_series[mask]

    #removing missing values
    clean_series = masked[masked.notnull()]

    return clean_series

def df_cleaner(dataframe):
    '''
    Returns a dataframe with clean data
    '''
    df_clean = pd.DataFrame()
    for column in dataframe.columns:
        df_clean['clean_'+ column] = series_cleaner(dataframe[column])
    return df_clean
