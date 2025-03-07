import streamlit as st

st.set_page_config(page_title="Data Report", layout="wide")

st.title("📊 Data Analysis Report")
st.sidebar.success("Select a sidebar above 🖕")

st.write("**Welcome to the data analysis dashboard. Use the sidebar to navigate between pages.**")
st.write("""This Data Analysis Report base on data file **fmi_weather_and_price.csv** which contains information about time, weather conditions and eletricity prices.
         \nThis interactive data visualization dashboard provides insights into Finnish electricity consumption, pricing trends, and temperature variations over a selected period. By analyzing real-world electricity usage data, the dashboard helps users understand how energy consumption fluctuates and how pricing impacts overall electricity costs.""")


# Display an image from a local file
st.image("Electricity-Towers.jpeg", caption="Electricity Weather", use_container_width=True)
