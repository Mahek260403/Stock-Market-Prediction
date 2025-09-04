# NIFTY 50 - Historical Stock Market Analysis & Forecasting  

A **Streamlit web app** for analyzing **NIFTY 50 stock market data** and forecasting future stock prices using **ARIMA (AutoRegressive Integrated Moving Average)**.  
Users can upload their own stock market CSV files and instantly explore historical trends, volatility, moving averages, and predictions.  

---

## Features  

✅ Upload multiple CSV files (merged automatically).  
✅ Interactive analysis with **matplotlib visualizations**.
✅ Forecasting with **ARIMA Model**.  
✅ Sidebar controls for data upload and forecast horizon. 
✅ Key insights:  
- Historical Closing Price  
- Daily Returns & Volatility  
- 50-Day & 200-Day Moving Averages  
 

---

## Techologies used :  

- **Python 3.9+**  
- **Streamlit** – Interactive Web App  
- **Pandas / NumPy** – Data Processing  
- **Matplotlib** – Visualizations  
- **Statsmodels** – ARIMA & Time Series Forecasting  

---

## Data Requirements  

Your CSV file(s) must contain at least these columns:  
- **Date** or **Timestamp** → Date of record  
- **Close** → Closing stock price  

Example:  

| Date       | Close   | Open  | High  | Low   | Volume   |  
|------------|---------|-------|-------|-------|----------|  
| 2020-01-01 | 12200.5 | 12210 | 12250 | 12180 | 2000000  |  
| 2020-01-02 | 12280.7 | 12250 | 12320 | 12230 | 2100000  |  

## Forecasting

The app uses ARIMA (1,1,1) model for short-term stock price forecasting.
Users can select the forecast horizon (5–60 days) using a slider.
	•	🔵 Blue Line → Historical Closing Prices
	•	🟠 Orange Line → Forecasted Prices

## How you can run it Locally

### 1️⃣ Clone the repository  


### 2️⃣ Create virtual environment & install dependencies
pip install -r requirements.txt

### 3️⃣ Run Streamlit app
streamlit run app.py

