import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="telecom_data",
            user="postgres",
            password="password"
        )
        print("Database connected successfully!")
        return conn
    except Exception as e:
        print(f"Error: {e}")
