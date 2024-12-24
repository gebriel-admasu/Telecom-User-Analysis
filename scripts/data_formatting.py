def format_columns(df, rename_map):
    """
    Rename columns based on a mapping dictionary.
    """
    return df.rename(columns=rename_map)

def convert_time_to_hours(df, column):
    """
    Convert time from seconds to hours.
    """
    df[f"{column}_hours"] = df[column] / 3600
    return df

def format_traffic_data(df, column):
    """
    Convert traffic data to GB.
    """
    df[f"{column}_GB"] = df[column] / (1024**2)
    return df
