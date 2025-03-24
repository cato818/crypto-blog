import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

class CryptoPricePredictor:
    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.scaler = StandardScaler()
        
    def prepare_data(self, data):
        """Prepara los datos normalizándolos"""
        if 'price' not in data.columns:
            raise ValueError("El DataFrame debe contener una columna 'price'")
        
        # Separar features y target
        features = data.drop('price', axis=1)
        target = data['price']
        
        # Normalizar features
        scaled_features = self.scaler.fit_transform(features)
        normalized_data = pd.DataFrame(
            scaled_features,
            columns=features.columns,
            index=features.index
        )
        
        return normalized_data, target
        
    def train(self, data):
        """Entrena el modelo con los datos proporcionados"""
        X, y = self.prepare_data(data)
        
        # Entrenar modelo
        self.model.fit(X, y)
        
        # Calcular métricas
        predictions = self.model.predict(X)
        feature_importance = self.model.feature_importances_
        
        return {
            'test_score': self.model.score(X, y),
            'feature_importance': feature_importance
        }
        
    def predict(self, X):
        """Realiza predicciones con el modelo entrenado"""
        if not hasattr(self.model, 'feature_importances_'):
            raise RuntimeError("El modelo debe ser entrenado antes de hacer predicciones")
            
        # Normalizar datos de entrada
        X_scaled = self.scaler.transform(X)
        
        # Hacer predicción
        return self.model.predict(X_scaled)