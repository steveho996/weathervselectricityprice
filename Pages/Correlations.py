import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("fmi_weather_and_price.csv", parse_dates=["Time"])

# Shift electricity price by -24 hours
df['Price_Shifted'] = df['Price'].shift(-24)
df = df.dropna()

# Title and Sidebar
st.title("📈 Statistics")
st.sidebar.header("📈 Statistics")
st.write("""In this page, data will be shown in descriptive statistics and correlation heatmap.
        
        \nDescriptive statistics provide a summary of key numerical values, such as the mean, median, standard deviation, and range of electricity prices, temperature, and wind speed. 
This helps us understand the overall distribution and variability of the data.
The correlation heatmap visually represents relationships between different variables. 

        \nBy analyzing these statistics and correlations, we can explore whether weather factors such as temperature and wind speed have an impact on electricity prices in Finland. 
This enables stakeholders to plan the use of electricity effectively, which leads to reduced operational costs.""")

# Descriptive Statistics
st.title("📊 Electricity Price & Weather Analysis in Finland")
st.write("### Descriptive Statistics")
st.write("""This table presents key descriptive statistics for three variables:
""Electricity Price (€/MWh), Temperature (°C), and Wind Speed (m/s), based on 23,015 hourly observations.""
\n 1/ Electricity prices show high variability, with occasional extreme spikes. 
The average price is relatively low (9.94 €/MWh), but fluctuations suggest sensitivity to external factors like demand, supply conditions, and energy policies.
\n 2/ Colder temperatures likely increase electricity demand, leading to potential price surges. The data shows temperatures dropping as low as -22.13°C, which may contribute to higher consumption for heating.
\n 3/ Wind speed influences electricity prices, as higher wind speeds may correlate with lower prices due to increased wind energy production. The data suggests wind speeds range between 1.33 m/s and 11.03 m/s, with relatively stable average conditions.
""")
st.write(df[['Price', 'Temp', 'Wind']].describe())

st.write("""While weather conditions (especially temperature and wind speed) appear to influence electricity prices, 
         further statistical modeling—such as correlation heatmaps and regression analysis—is needed to confirm their impact and predictive strength.""")

# Correlation Heatmap
st.write("### Correlation Heatmap")
st.write("""This table presents key descriptive statistics for three variables:
\n A positive correlation (closer to +1) means that as one variable increases, the other tends to increase as well, while a negative correlation (closer to -1) indicates an inverse relationship. 
A correlation near 0 suggests little to no relationship.
\n 1/ Temperature has a weak positive correlation (0.15) with electricity prices, meaning that as temperature increases, prices tend to rise slightly. However, the relationship is weak, suggesting that other factors (such as demand, energy production, or external economic conditions) play a more significant role.
\n 2/ Wind speed has almost no correlation (-0.02) with electricity prices, implying that fluctuations in wind speed alone do not have a direct impact on pricing. This may be due to Finland’s energy mix, where wind power is not the dominant pricing factor.
\n 3/ Temperature and wind speed have a slight negative correlation (-0.077), meaning that higher temperatures are slightly associated with lower wind speeds, though the relationship is weak.""")

fig, ax = plt.subplots()
sns.heatmap(df[['Price', 'Temp', 'Wind']].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
