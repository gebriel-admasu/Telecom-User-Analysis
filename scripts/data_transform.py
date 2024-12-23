from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def perform_clustering(df, columns, n_clusters):
    """
    Perform KMeans clustering on specified columns.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    df['cluster'] = kmeans.fit_predict(df[columns])
    return df, kmeans

def aggregate_data(df, group_by_column, agg_column, agg_func):
    """
    Perform aggregation (sum, mean, etc.) grouped by a specific column.
    """
    return df.groupby(group_by_column)[agg_column].agg(agg_func).reset_index()

def top_n_values(df, column, n):
    """
    Return the top N values of a specific column.
    """
    return df.nlargest(n, column)







