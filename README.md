# OnionTrends
OnionTrends is an AI/ML-based project designed to predict onion prices using historical data, weather conditions, and buffer stock levels.

Key Features
* Price Prediction: Predicts onion prices using historical data and external factors like weather and buffer stock levels.
* Buffer Stock Integration: Incorporates buffer stock data to analyze the impact of market interventions on price stability.
* Multiple Models: Compares the performance of Random Forest, LSTM, and ARIMA models for accurate predictions.
* Real-Time Predictions: Allows users to input new data and get real-time price forecasts.
* Visualizations: Provides interactive visualizations of price trends, buffer stock levels, and model performance.

Technologies Used
* Programming Language: Python
* Libraries/Frameworks:
* Machine Learning: Scikit-learn, TensorFlow/Keras, Statsmodels
* Data Handling: Pandas, NumPy]
* Visualization: Matplotlib, Seaborn
* Model Saving: Joblib
* Development Environment: Google Colab
* Deployment (Optional): Streamlit, Flask

Dataset
The project uses a synthetic dataset for demonstration purposes, which includes:
* Onion Price Data: Daily wholesale and retail prices.
* Buffer Stock Data: Buffer stock levels and market interventions (e.g., release or addition of stock).

How It Works
1. Data Collection: Historical price data, weather data, and buffer stock levels are collected and preprocessed.
2. Feature Engineering: Additional features like lagged prices and rolling averages are created.
3. Model Training: Multiple models (Random Forest, LSTM, ARIMA) are trained and evaluated.
4. Prediction: The best-performing model is used to predict onion prices for new input data.
5. Visualization: Results are visualized to provide insights into price trends and buffer stock impact.

Steps to run this project
1. Clone the Repository:
   * git clone https://github.com/yHarsh5606/OnionTrends.git
2. Install the required libaries
3. Now run the app.py
   * streamlit run app.py
