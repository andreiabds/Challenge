from Metrics import fill_list, true_fill_list, cardinality_list, unique_values_list
from DataCleaning import df_cleaner, series_cleaner
#import matplotlib as plt
import numpy as np
import pandas as pd
#import seaborn as sbs

df = pd.read_json('data_analysis.json')


def df1_unique():
    unique = pd.DataFrame()
    unique['features'] = df.columns
    unique['unique_values'] = unique_values_list(df)
    df1 = unique.sort_values('unique_values').reset_index(drop=True)
    return df1

def df2_metrics():
    #DATAFRAME metrics
    df_result = pd.DataFrame()
    df_result['features'] = df.columns
    df_result['old_cardinality'] = unique_values_list(df)
    df_result['true_cardinality'] = cardinality_list(df)
    df_result['diff_cardinality'] = df_result['old_cardinality'] - df_result['true_cardinality']
    df_result['fill_data'] = fill_list(df)
    df_result['fill_rate'] = (df_result['fill_data']/len(df))
    df_result['true_fill_data'] = true_fill_list(df)
    df_result['true_fill_rate'] = df_result['true_fill_data'] /len(df)
    df_result['diff_fill_data'] = df_result['fill_data'] - df_result['true_fill_data']

    pd.options.display.float_format = '{:.4f}'.format
    return df_result



if __name__ == '__main__':

    df_result = df2_metrics()
    # fill_rate = df_result[['features','fill_data', 'fill_rate']]
    # true_fill_rate = df_result[['features','true_fill_data', 'true_fill_rate']]
    # cardinality = df_result[['features', 'true_cardinality']].sort_values('true_cardinality').reset_index(drop=True)

    print df_result
