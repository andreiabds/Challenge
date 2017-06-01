import pandas as pd
from DataCleaning import series_cleaner

def fill_list(dataframe):
    '''
    Returns a list with the fill rate (number of records that have a value) of
    each column in the dataframe.
    '''
    return [dataframe[column].count()for column in dataframe.columns]

def true_fill_list(dataframe):
    '''
    Returns a list with the true fill rate (number of records that have a valid
    value) of each column in the dataframe.
    '''
    return [len(series_cleaner(dataframe[column])) for column in dataframe.columns]

def cardinality_list(dataframe):
    '''
    Returns a list with the cardinality number of each column in the dataframe.
    '''
    return [len(series_cleaner(dataframe[column]).unique()) for column in dataframe.columns]

def unique_values_list(dataframe):
    '''
    Returns a list with the cardinality number of each column in the dataframe.
    Data is processed previous to cleaning.
    '''
    return [len(dataframe[column].unique()) for column in dataframe.columns]
