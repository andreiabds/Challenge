from CreatingDF import df1_unique, df2_metrics
from DataCleaning import series_cleaner, df_cleaner
from Metrics import fill_list, true_fill_list, cardinality_list, unique_values_list

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbs


if __name__ == '__main__':
    print 'reading df'
    df = pd.read_json('data_analysis.json')
    df_unique = df1_unique()
    df_result = df2_metrics
    df_clean = df_cleaner(df)

    print "preparing Plot 1"
    #PLOT 1 Unique Values Distribution
    #plot1 = df_unique.plot.bar(x=df_unique['features'])
    # plot1 = plt.plot(df_unique['features'], df_unique['unique_values'])
    # plt.show
    #
    # #PLOT 2
    # true_fill_rate = df_result[['features','true_fill_data']]
    # graph_rate = true_fill_rate.sort(columns='true_fill_data')
    # ax = graph_rate.plot(x=graph_rate['features'], kind='bar', title='True-Valued Fill Rate', sort_columns=True, legend=False)
    # ax.set_ylabel("Number of Good Data Records")

    # #PLOT 3
    # #PLOT revenue distribution for all clean data
    #
    df_revenue = df_clean['clean_revenue'].value_counts().sort_values(ascending=False)
    df_revenue = df_revenue.reindex(index = [u'less than $500,000', u'$500,000 to $1 million', u'$1 to 2.5 million',
           u'$2.5 to 5 million', u'$5 to 10 million', u'$10 to 20 million',
           u'$20 to 50 million', u'$50 to 100 million', u'$100 to 500 million',
            u'over $500 million', u'over $1 billion'])
    df_revenue.plot(kind='bar', title='Revenue')
    plt.show()

    #PLOT 4 headcount distribution for all clean data

    headcount = df_clean['clean_headcount'].value_counts().sort_values(ascending=False)
    headcount = headcount.reindex(index = [u'1 to 4', u'5 to 9', u'10 to 19', u'20 to 49', u'50 to 99',
           u'100 to 249', u'250 to 499', u'500 to 999', u'over 1,000'])
    headcount.plot(kind='bar', title='Headcount')
    plt.show()


    #PLOT 5 time_in_business distribution for all clean data
    time = df_clean['clean_time_in_business'].value_counts().sort_values(ascending=False)
    time.plot(kind='bar', title='Time in Business')
    plt.show()

    #PLOT 6 Analyzing Billionaires
    billion = df_clean[df_clean['clean_revenue']=='over $1 billion']
    s = billion['clean_headcount'].value_counts()
    s = s.reindex(index = [u'1 to 4', u'5 to 9', u'10 to 19', u'20 to 49', u'50 to 99',
           u'100 to 249', u'250 to 499', u'500 to 999', u'over 1,000'])
    s.plot(kind='bar', title= "Headcount in Businesses with Over $1 billion Revenue")
    plt.show()

    min_billion = billion[billion['clean_headcount']=='1 to 4']
    print min_billion['clean_name'].value_counts().sort_values(ascending=False)
