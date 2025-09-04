import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# --- Streamlit Page Setup ---
st.set_page_config(page_title="NIFTY 50 - Historical Stock Analysis", layout="wide")
st.title("NIFTY 50 - Historical Stock Analysis & Prediction System")

# --- Sidebar Section ---
st.sidebar.header("📂 Upload Data")
uploaded_files = st.sidebar.file_uploader(
    "Upload your CSV files ", 
    type=["csv"], 
    accept_multiple_files=True
)

st.sidebar.markdown("""
---
## ℹ️ Instructions
- Upload one or more CSV files.
- Required columns: **Date** (or Timestamp) and **Close**.
""")

if uploaded_files:
    # Read and merge all uploaded CSVs
    dfs = [pd.read_csv(file) for file in uploaded_files]
    data = pd.concat(dfs, ignore_index=True).drop_duplicates()

    # --- Standardize Column Names ---
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]

    # --- Identify Date Column ---
    possible_date_cols = ['date', 'timestamp']
    date_col = None
    for col in possible_date_cols:
        if col in data.columns:
            date_col = col
            break

    if not date_col:
        st.error(" No date column found in the CSV(s). Please make sure your data has a 'Date' or 'Timestamp' column.")
        st.stop()

    # Rename for consistency
    data.rename(columns={date_col: 'date'}, inplace=True)

    # Convert to datetime
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data.dropna(subset=['date'], inplace=True)

    # Ensure Close column exists
    if 'close' not in data.columns:
        st.error(" No 'Close' column found in the CSV(s). Please make sure your data has a 'Close' column.")
        st.stop()

    # Sort data
    data.sort_values('date', inplace=True)
    data.reset_index(drop=True, inplace=True)

    # --- Plot Closing Price ---
    st.subheader("1.Historical Closing Price")
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(data['date'], data['close'], label='Close', color='blue')
    ax.set_title("Closing Price Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    st.pyplot(fig)

    # --- Daily Returns & Volatility ---
    data['daily_return'] = data['close'].pct_change()
    data['volatility'] = data['daily_return'].rolling(window=30).std()

    st.subheader("2.Daily Returns & 30-Day Rolling Volatility")
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots()
        ax.plot(data['date'], data['daily_return'], alpha=0.5, color='orange')
        ax.axhline(0, linestyle='--', color='black')
        ax.set_title("Daily Returns")
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        ax.plot(data['date'], data['volatility'], color='red')
        ax.set_title("30-Day Rolling Volatility")
        st.pyplot(fig)

    # --- Moving Averages ---
    st.subheader("3.Moving Averages")
    data['MA50'] = data['close'].rolling(window=50).mean()
    data['MA200'] = data['close'].rolling(window=200).mean()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(data['date'], data['close'], label='Close Price', alpha=0.6)
    ax.plot(data['date'], data['MA50'], label='50-Day MA', color='green')
    ax.plot(data['date'], data['MA200'], label='200-Day MA', color='red')
    ax.set_title("Moving Averages")
    ax.legend()
    st.pyplot(fig)

    # --- Final Snapshot ---
    st.subheader("4. Latest Data Snapshot")
    st.dataframe(data.tail(10))

    # --- Forecasting Section ---
    st.subheader("5.Forecasting with ARIMA Model")

    n_days = st.slider("Select number of days to forecast", 5, 60, 30)

    try:
        # Prepare close price series
        close_prices = data['close']

        # Fit ARIMA model
        model = ARIMA(close_prices, order=(1, 1, 1))
        result = model.fit()

        # Forecast future values
        forecast = result.forecast(steps=n_days)

        # Build forecast dataframe
        forecast_dates = pd.date_range(start=data['date'].iloc[-1] + pd.Timedelta(days=1), periods=n_days)
        forecast_df = pd.DataFrame({"date": forecast_dates, "forecasted_close": forecast.values})

        # Plot historical vs forecast
        fig, ax = plt.subplots(figsize=(12,5))
        ax.plot(data['date'], data['close'], label="Historical Close", color="blue")
        ax.plot(forecast_df['date'], forecast_df['forecasted_close'], label="Forecast", color="orange")
        ax.set_title(f"{n_days}-Day Stock Price Forecast (ARIMA)")
        ax.legend()
        st.pyplot(fig)

        # Show forecast table
        st.dataframe(forecast_df)

    except Exception as e:
        st.warning(" Could not generate forecast.")
        st.text(str(e))

else:
    st.info("📂 Upload one or more CSV files in the **sidebar** to begin the analysis.")