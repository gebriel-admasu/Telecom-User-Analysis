import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch DB credentials
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Database connection
def get_data(query):
    connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

# Sidebar for navigation
st.sidebar.title("Telecom Data Dashboard")
page = st.sidebar.radio(
    "Select a Page",
    ("User Overview Analysis", "User Engagement Analysis", "Experience Analysis", "Satisfaction Analysis")
)

# User Overview Analysis Page
# User Overview Analysis Page
if page == "User Overview Analysis":
    st.title("User Overview Analysis")
    st.write("Visualizing user overview insights.")
    
    # Query to get top 10 handset types from the xdr_data table
    query = """
    SELECT "Handset Type", COUNT(*) AS handset_count
    FROM xdr_data
    GROUP BY "Handset Type"
    ORDER BY handset_count DESC
    LIMIT 10;
    """
    
    # Fetch the data
    data = get_data(query)

    # Check if data is retrieved
    if data.empty:
        st.error("No data found for Handset Type analysis.")
    else:
        # Display raw data
        st.write("Top 10 Handset Types:")
        st.dataframe(data)

        # Plot bar chart
        st.bar_chart(data.set_index("Handset Type")["handset_count"])


# User Engagement Analysis Page
elif page == "User Engagement Analysis":
    st.title("User Engagement Analysis")
    st.write("Visualizing user engagement insights.")
    data = get_data("SELECT * FROM customer_satisfaction;")  # Replace with actual query
    st.write(data.head())
    st.line_chart(data['engagement_score'])  # Example chart



# Experience Analysis Page
elif page == "Experience Analysis":
    st.title("Experience Analysis")
    st.write("Visualizing user experience insights.")
    
    # Load data
    data = get_data("SELECT * FROM customer_satisfaction;")  # Replace with your actual query
    
    # Check if the 'Cluster' column exists
    if 'Cluster' not in data.columns:
        st.error("The 'Cluster' column is missing. Ensure clustering is performed.")
    else:
        # Create a Matplotlib figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot boxplot with Seaborn
        sns.boxplot(data=data, x='Cluster', y='experience_score', ax=ax)
        ax.set_title("Experience Score by Cluster")
        ax.set_xlabel("Cluster")
        ax.set_ylabel("Experience Score")
        
        # Render the plot in Streamlit
        st.pyplot(fig)


# Satisfaction Analysis Page
elif page == "Satisfaction Analysis":
    st.title("Satisfaction Analysis")
    st.write("Visualizing customer satisfaction.")
    data = get_data("SELECT * FROM customer_satisfaction;")  # Replace with actual query
    st.write(data.head())
    st.scatter_chart(data[['engagement_score', 'satisfaction_score']])  # Example chart
# Add a slider to filter data by satisfaction score
    satisfaction_threshold = st.slider("Satisfaction Score Threshold", 0.0, 1.0, 0.5)
    filtered_data = data[data['satisfaction_score'] >= satisfaction_threshold]
    st.write(filtered_data)
