import pandas as pd
import numpy as np


def clean_numeric_columns(df, columns):
    """
    Ensure numeric columns have valid values.
    """
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def remove_outliers(df, column, threshold):
    """
    Remove outliers based on a threshold.
    """
    return df[df[column] <= threshold]



