---
noteId: "4b95f0d0395011f0ab84adad625be36c"
tags: []

---

# 📈 Stock Market Dashboard & Prediction System

A real-time web application that tracks **NIFTY 50 index** and predicts **next-day trends** using machine learning models like **LSTM** — all wrapped in an interactive **Streamlit dashboard**.

---

## 🚀 Features

- 📊 **Live NIFTY 50 Data** using `yfinance`
- 🤖 **LSTM-based Model** for predicting next-day NIFTY trend
- 🌐 **Streamlit Web App** for real-time visualization
- 📉 Historical data visualization with interactive graphs

---

## 🧪 Technologies Used

| Category        | Stack/Tools                     |
|----------------|----------------------------------|
| Data            | `yfinance`, `pandas`, `numpy`    |
| Dashboard       | `Streamlit`, `Plotly`            |
| ML Model        | `TensorFlow` / `Keras`, `scikit-learn` |
| Deployment      | GitHub, Streamlit Cloud (optional) |

---

## 🖼️ Dashboard Preview

![Dashboard Preview](images/dashboard-screenshot.png)

---

## 📂 Project Structure


Stock_Market_Prediction/
│
├── app.py # Streamlit app
├── model.py # LSTM training & prediction
├── requirements.txt
├── .gitignore
└── README.md