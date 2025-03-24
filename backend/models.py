from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import joblib
import os

class CryptoPricePredictor:
    def __init__(self):
        """Inicializa el predictor con un modelo RandomForest"""
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )
        self.scaler = MinMaxScaler()
        
    def prepare_data(self, data):
        """Prepara los datos normalizándolos."""
        if 'price' not in data.columns:
            raise ValueError("El DataFrame debe contener una columna 'price'")
        
        # Normalizar features
        features = data.drop('price', axis=1)
        scaled_features = self.scaler.fit_transform(features)
        normalized_data = pd.DataFrame(
            scaled_features, 
            columns=features.columns, 
            index=features.index
        )
        
        return normalized_data, data['price']

    def train(self, data, test_size=0.2):
        """Entrena el modelo con los datos proporcionados."""
        # Preparar datos
        X, y = self.prepare_data(data)
        
        # Split de datos
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # Entrenar modelo
        self.model.fit(X_train, y_train)
        
        # Calcular métricas
        train_score = self.model.score(X_train, y_train)
        test_score = self.model.score(X_test, y_test)
        
        return {
            'train_score': train_score,
            'test_score': test_score,
            'feature_importance': dict(zip(X.columns, self.model.feature_importances_))
        }

    def predict(self, features):
        """Predice el precio basado en las características proporcionadas."""
        if not isinstance(features, pd.DataFrame):
            raise ValueError("Las características deben ser un DataFrame")
            
        # Normalizar features usando el mismo scaler
        scaled_features = self.scaler.transform(features)
        scaled_features_df = pd.DataFrame(scaled_features, columns=features.columns)
        
        return self.model.predict(scaled_features_df)

    def save_model(self, filename):
        """Guarda el modelo entrenado y el scaler."""
        model_path = f"{filename}_model.joblib"
        scaler_path = f"{filename}_scaler.joblib"
        
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)

    def load_model(self, filename):
        """Carga un modelo entrenado y su scaler."""
        model_path = f"{filename}_model.joblib"
        scaler_path = f"{filename}_scaler.joblib"
        
        if not os.path.exists(model_path) or not os.path.exists(scaler_path):
            raise FileNotFoundError("No se encontraron los archivos del modelo")
            
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)