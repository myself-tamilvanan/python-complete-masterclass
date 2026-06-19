# Chapter 41: Streamlit Tutorial
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:01:35
# ============================================
# To run: pip install streamlit && streamlit run program.py

# -----------------------------------------------
# STREAMLIT APP - Save this as app.py and run:
# streamlit run app.py
# -----------------------------------------------

STREAMLIT_APP = """
import streamlit as st
import pandas as pd
import numpy as np
import time

# Page configuration
st.set_page_config(
    page_title="Python Dashboard",
    page_icon="Ì†ΩÌ∞ç",
    layout="wide"
)

# -----------------------------------------------
# Title and Introduction
# -----------------------------------------------
st.title("Ì†ΩÌ∞ç Python Data Dashboard")
st.markdown("Built with **Streamlit** - No frontend knowledge needed!")

# -----------------------------------------------
# Sidebar Controls
# -----------------------------------------------
st.sidebar.header("Controls")
num_rows = st.sidebar.slider("Number of data points", 10, 200, 50)
chart_type = st.sidebar.selectbox("Chart type", ["Line", "Bar", "Area"])
show_raw = st.sidebar.checkbox("Show raw data", value=False)

# -----------------------------------------------
# Generate Sample Data
# -----------------------------------------------
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=num_rows)
data = pd.DataFrame({
    "Sales": np.random.randint(100, 500, num_rows).cumsum(),
    "Costs": np.random.randint(50, 300, num_rows).cumsum(),
    "Profit": np.random.randint(10, 200, num_rows).cumsum()
}, index=dates)

# -----------------------------------------------
# Main Content
# -----------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"${data['Sales'].iloc[-1]:,}", delta="‚Üë12%")
with col2:
    st.metric("Total Costs", f"${data['Costs'].iloc[-1]:,}", delta="‚Üë8%")
with col3:
    profit = data['Sales'].iloc[-1] - data['Costs'].iloc[-1]
    st.metric("Net Profit", f"${profit:,}", delta="‚Üë5%")

st.divider()

# Chart
st.subheader(f"{chart_type} Chart")
if chart_type == "Line":
    st.line_chart(data)
elif chart_type == "Bar":
    st.bar_chart(data["Sales"])
else:
    st.area_chart(data)

# Raw Data
if show_raw:
    st.subheader("Raw Data")
    st.dataframe(data.tail(20))

# -----------------------------------------------
# Interactive Section
# -----------------------------------------------
st.subheader("Calculate BMI")
col_a, col_b = st.columns(2)
with col_a:
    weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
with col_b:
    height = st.number_input("Height (m)", 1.0, 2.5, 1.75)

bmi = weight / height ** 2
if st.button("Calculate"):
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    st.success(f"BMI: {bmi:.1f} - {category}")

# File Upload
st.subheader("Upload CSV Data")
uploaded = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df)
    st.download_button("Download data", df.to_csv(), "data.csv")
"""

# Print the app code for reference
print("Streamlit App Code:")
print("="*50)
print("Save as app.py and run: streamlit run app.py")
print("="*50)
print()
print(STREAMLIT_APP[:1500])
print("...and more. See full code in STREAMLIT_APP variable.")

# Standalone demo (no Streamlit needed)
print("\n--- Standalone Demo (simulated output) ---")

import random
data_points = 50
sales = [random.randint(100, 500) for _ in range(data_points)]
total = sum(sales)
print(f"Total Sales: ${total:,}")
print(f"Average: ${total//data_points:,}")
print(f"Max: ${max(sales):,}")
print(f"Min: ${min(sales):,}")

print("\n" + "="*50)
print("Chapter 41 Complete!")
print("Install streamlit: pip install streamlit")
print("Run: streamlit run program.py")
print("="*50)