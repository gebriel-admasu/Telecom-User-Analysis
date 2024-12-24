import sqlite3
import pandas as pd

def connect_to_database(db_path):
    """
    Establish a connection to the SQLite database.
    """
    conn = sqlite3.connect(db_path)
    print("Database connection successful")
    return conn

def fetch_data_from_table(conn, table_name):
    """
    Fetch data from a specific table in the database.
    """
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql_query(query, conn)
