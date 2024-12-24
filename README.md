# Telecom-User-Analysis
# **Telecom User Analytics Project**

## **Project Overview**
This project aims to analyze telecom user data to derive actionable insights about customer behavior, engagement, and satisfaction. It leverages Python for data processing and visualization and includes an interactive dashboard to showcase results. The project is divided into five main tasks:

1. **User Overview Analysis**
2. **User Engagement Analysis**
3. **Experience Analysis**
4. **Satisfaction Analysis**
5. **Dashboard Development**

---

## **Project Structure**
```
Telecom-User-Analytics/
├── data/
│   ├── xdr_data.csv             # Original dataset
│   ├── final_results.csv        # Processed results for dashboard
├── scripts/
│   ├── data_cleaning.py         # Functions for cleaning data
│   ├── data_extraction.py       # Functions for database queries
│   ├── data_transform.py        # Functions for data transformations
│   ├── data_analysis.py         # Functions for analysis and clustering
├── dashboard/
│   ├── app.py                   # Dash app script for dashboard
│   ├── elbow_method.csv         # Data for determining optimal k in clustering
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── presentation/
    ├── project_report.pdf       # Project report
    ├── presentation_slides.pptx # Presentation slides
```

---

## **Setup Instructions**

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Telecom-User-Analytics.git
   cd Telecom-User-Analytics
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **Step 1: Data Extraction**
- Update your `.env` file with PostgreSQL credentials:
  ```env
  DB_HOST=localhost
  DB_PORT=5432
  DB_NAME=telecom_data
  DB_USER=postgres
  DB_PASSWORD=password
  ```
- Extract data using:
  ```bash
  python scripts/data_extraction.py
  ```

### **Step 2: Data Cleaning and Transformation**
- Run cleaning and transformation scripts:
  ```bash
  python scripts/data_cleaning.py
  python scripts/data_transform.py
  ```

### **Step 3: Analysis and Clustering**
- Perform user segmentation and save results:
  ```bash
  python scripts/data_analysis.py
  ```

### **Step 4: Dashboard Deployment**
- Navigate to the `dashboard/` folder and run the app:
  ```bash
  cd dashboard
  python app.py
  ```
- Open the provided URL in your browser (e.g., `http://127.0.0.1:8050`).

---

## **Features**

### **1. User Overview Analysis**
- Exploratory data analysis (EDA) with variable descriptions and correlations.
- PCA for dimensionality reduction.

### **2. User Engagement Analysis**
- Aggregation of engagement metrics (session frequency, duration, total traffic).
- Clustering users into engagement levels using K-means.

### **3. Experience Analysis**
- Analysis of network parameters (e.g., TCP retransmissions, RTT, throughput).
- Clustering based on experience scores.

### **4. Satisfaction Analysis**
- Calculation of satisfaction scores combining engagement and experience metrics.
- Identification of top satisfied customers.

### **5. Dashboard Development**
- Interactive dashboard with:
  - Tabs for each task.
  - Graphs for KPIs and clustering insights.

---

## **Limitations**
- Missing values in key columns like handset type.
- Analysis limited to available metrics and time frame.
- Clustering assumes optimal k based on elbow method; real-world validation needed.

---

## **Acknowledgments**
- Tools: Python, Dash, Plotly, PostgreSQL.
- Libraries: Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib.

---

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.

---

## **Contact**
For questions or feedback, please contact:
- Name: [Your Name]
- Email: [Your Email]
- GitHub: [Your GitHub Profile]
