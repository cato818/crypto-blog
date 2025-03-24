import numpy as np
import pandas as pd
from sklearn import __version__ as sklearn_version  # Importación correcta de la versión
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import joblib
import os
from model import CryptoPricePredictor

def test_imports():
    """Prueba que todas las dependencias estén correctamente instaladas"""
    print("Probando importaciones:")
    print(f"NumPy versión: {np.__version__}")
    print(f"Pandas versión: {pd.__version__}")
    print(f"Scikit-learn versión: {sklearn_version}")  # Uso correcto de la versión importada
    
    # Probar creación de instancia del predictor
    predictor = CryptoPricePredictor()
    print("\nCreación de instancia CryptoPricePredictor exitosa!")
    
    print("\nTodas las importaciones fueron exitosas!")

if __name__ == "__main__":
    test_imports()