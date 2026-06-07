# Chapter 41: Streamlit Tutorial

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:01:35

## Overview
Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science — with zero frontend knowledge needed.

## Installation
```bash
pip install streamlit
```

## Running a Streamlit App
```bash
streamlit run app.py
```

## Key Widgets
| Widget          | Code                              |
|----------------|-----------------------------------|
| Title/Header    | st.title(), st.header()           |
| Text            | st.text(), st.write(), st.markdown()|
| Text input      | st.text_input("Label")            |
| Number input    | st.number_input("Label")          |
| Slider          | st.slider("Label", min, max)      |
| Button          | st.button("Click me")             |
| Checkbox        | st.checkbox("Enable")             |
| Selectbox       | st.selectbox("Choose", options)   |
| File upload     | st.file_uploader("Upload")        |
| Data frame      | st.dataframe(df)                  |
| Chart           | st.line_chart(data)               |
| Sidebar         | st.sidebar.widget()               |

## Learning Outcomes
- Build interactive web apps with Streamlit
- Create data dashboards
- Add charts and visualizations
- Accept user inputs and display results