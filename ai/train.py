import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import sqlite3
from datetime import datetime

# Function to fetch cryptocurrency data from an API
def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30'
    response = requests.get(url)
    data = response.json()
    prices = data['prices']
    return pd.DataFrame(prices, columns=['timestamp', 'price'])

# Function to preprocess the data
def preprocess_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df['price'] = df['price'].astype(float)
    df['target'] = df['price'].shift(-1)
    df.dropna(inplace=True)
    return df

# Function to train the predictive model
def train_model():
    df = fetch_crypto_data()
    df = preprocess_data(df)
    
    X = df[['price']]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, 'crypto_price_model.pkl')
    
    # Save predictions to the database
    save_predictions_to_db(model, X_test)

# Function to save predictions to the SQLite database
def save_predictions_to_db(model, X_test):
    predictions = model.predict(X_test)
    conn = sqlite3.connect('../backend/database.db')
    cursor = conn.cursor()
    
    for price, prediction in zip(X_test['price'], predictions):
        cursor.execute("INSERT INTO predictions (price, predicted_price, created_at) VALUES (?, ?, ?)",
                       (price, prediction, datetime.now()))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    train_model()