def compute_top_bottom_most_frequent(df, column):
    """
    Compute the top 10, bottom 10, and most frequent values of a column.
    """
    top_10 = df[column].nlargest(10)
    bottom_10 = df[column].nsmallest(10)
    most_frequent = df[column].value_counts().head(10)
    return top_10, bottom_10, most_frequent