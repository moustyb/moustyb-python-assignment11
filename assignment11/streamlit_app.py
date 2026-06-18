import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Page Configuration and Title
st.set_page_config(page_title="Capstone Dashboard", layout="wide")
st.title("📊 Web Scraping Capstone Dashboard")
st.markdown("Welcome! This dashboard visualizes data from our SQLite database. Use the sidebar to filter the data.")

# 2. Load Data from Database
@st.cache_data # This makes the app run faster by caching the data
def load_data():
    try:
        # Path for Streamlit Cloud (repo root)
        conn = sqlite3.connect('db/lesson.db')
    except:
        # Path for local testing if script is in a subfolder
        conn = sqlite3.connect('../db/lesson.db')

    # Query 1: Employee Revenue
    emp_query = """
    SELECT e.last_name, SUM(p.price * l.quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id
    """
    emp_df = pd.read_sql_query(emp_query, conn)

    # Query 2: Product Sales
    prod_query = """
    SELECT p.product_name, SUM(l.quantity) as total_sold
    FROM products p
    JOIN line_items l ON p.product_id = l.product_id
    GROUP BY p.product_name
    """
    prod_df = pd.read_sql_query(prod_query, conn)

    conn.close()
    return emp_df, prod_df

emp_df, prod_df = load_data()

# 3. Sidebar Interactions (Required by Rubric)
st.sidebar.header("🔍 Filter Data")

# Interaction 1: Dropdown Selectbox
selected_employee = st.sidebar.selectbox(
    "Select an Employee:", 
    emp_df['last_name'].unique()
)

# Interaction 2: Slider
min_revenue = st.sidebar.slider(
    "Minimum Revenue Threshold ($):", 
    0, 
    int(emp_df['revenue'].max()), 
    0
)

# 4. Main Dashboard Content
st.header("1. Revenue Overview")
col1, col2 = st.columns(2)

# Visualization 1: Bar Chart & Metric
with col1:
    st.metric(label="Total Company Revenue", value=f"${emp_df['revenue'].sum():,.2f}")
    fig_bar = px.bar(
        emp_df, 
        x='last_name', 
        y='revenue', 
        color='revenue', 
        title="Revenue by Employee"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Visualization 2: Pie Chart & Metric
with col2:
    selected_rev = emp_df[emp_df['last_name'] == selected_employee]['revenue'].values[0]
    st.metric(label=f"Revenue for {selected_employee}", value=f"${selected_rev:,.2f}")
    fig_pie = px.pie(
        prod_df, 
        values='total_sold', 
        names='product_name', 
        title="Product Sales Distribution"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Visualization 3: Interactive Data Table
st.header("2. Detailed Data Table")
st.markdown("Use the slider in the sidebar to filter employees by minimum revenue.")
filtered_emp = emp_df[emp_df['revenue'] >= min_revenue]
st.dataframe(filtered_emp, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Dashboard created for Assignment 11 - Task 6")
