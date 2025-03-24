import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class CryptoDataLoader:
    def __init__(self, symbol='BTC-USD'):
        self.symbol = symbol
        
    def get_historical_data(self, period='1y'):
        """Obtiene datos históricos de Yahoo Finance"""
        try:
            print(f"Descargando datos de {self.symbol}...")
            ticker = yf.Ticker(self.symbol)
            data = ticker.history(period=period)
            
            if data.empty:
                print(f"No se encontraron datos para {self.symbol}")
                return None
                
            print(f"✓ Datos descargados: {len(data)} registros")
            return data
            
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return None
            
    def prepare_training_data(self, data):
        """Prepara los datos para el entrenamiento"""
        if data is None:
            return None, None
            
        print("Preparando datos...")
        
        # Calcular indicadores técnicos
        data['SMA_7'] = data['Close'].rolling(window=7).mean()
        data['SMA_30'] = data['Close'].rolling(window=30).mean()
        data['Volatility'] = data['Close'].rolling(window=7).std()
        
        # Crear features
        features = pd.DataFrame({
            'precio_anterior': data['Close'].shift(1),
            'volumen': data['Volume'],
            'sma_7': data['SMA_7'],
            'sma_30': data['SMA_30'],
            'volatilidad': data['Volatility']
        })
        
        # Target variable
        target = data['Close']
        
        # Eliminar filas con NaN
        features = features.dropna()
        target = target[features.index]
        
        print(f"✓ Datos preparados: {len(features)} registros")
        return features, target