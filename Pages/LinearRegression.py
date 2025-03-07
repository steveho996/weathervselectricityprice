import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# Load dataset
df = pd.read_csv("fmi_weather_and_price.csv", parse_dates=["Time"])

# Shift electricity price by -24 hours
df['Price_Shifted'] = df['Price'].shift(-24)
df = df.dropna()

# Title
st.title("📊 Electricity Price & Weather Analysis in Finland")
st.sidebar.header("📈 Regression Charts")

# Regression Analysis
X = df[['Temp', 'Wind']]
y = df['Price_Shifted']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

st.write(f"### Linear Regression Model (R² Score: {r2:.4f})")

# Scatter plot of Actual vs Predicted Prices
st.write("### Actual vs Predicted Electricity Prices")
fig, ax = plt.subplots()
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5, ax=ax)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')
ax.set_xlabel("Actual Prices (€/MWh)")
ax.set_ylabel("Predicted Prices (€/MWh)")
st.pyplot(fig)

st.write("### Impact of Temperature on Price")
st.write("""Based on the provided visualization, a scatter plot, the analysis reveals a significant relationship between temperature and electricity prices.
\n The visualization demonstrates an inverse correlation between temperature speed and electricity prices:
\n 1/ Higher wind speeds lead to lower and more stable electricity prices.
\n 2/ Low wind speeds are linked to greater price volatility and higher costs.""")

fig, ax = plt.subplots()
sns.regplot(x=df['Temp'], y=df['Price'], scatter_kws={'alpha':0.3}, line_kws={"color": "red"}, ax=ax)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Electricity Price (€/MWh)")
st.pyplot(fig)

st.write("### Impact of Wind speed on Price")
st.write("""Based on the provided visualization, a scatter plot, the analysis reveals a significant relationship between wind speed and electricity prices.
\n Higher wind speeds are linked to lower and more stable electricity prices, likely reflecting the cost benefits of increased wind energy production. 
\n Conversely, low wind speeds result in higher and more volatile prices, emphasizing the challenges of limited renewable energy availability during calm periods..""")
fig, ax = plt.subplots()
sns.regplot(x=df['Wind'], y=df['Price'], scatter_kws={'alpha':0.3}, line_kws={"color": "red"}, ax=ax)
ax.set_xlabel("Wind Speed (m/s)")
ax.set_ylabel("Electricity Price (€/MWh)")
st.pyplot(fig)
