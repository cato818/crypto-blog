import pandas as pd
import numpy as np
from model import CryptoPricePredictor
from data_loader import CryptoDataLoader

def test_model_with_real_data():
    """Prueba el modelo con datos reales de Bitcoin"""
    print("Iniciando prueba del modelo con datos reales...")
    
    # Cargar datos
    loader = CryptoDataLoader('BTC-USD')
    data = loader.get_historical_data()
    
    if data is None:
        print("Error: No se pudieron obtener los datos")
        return
    
    # Preparar datos
    X, y = loader.prepare_training_data(data)
    training_data = pd.concat([X, pd.Series(y, name='price')], axis=1)
    
    # Crear y entrenar modelo
    predictor = CryptoPricePredictor()
    
    try:
        # Entrenar modelo
        print("\nEntrenando modelo...")
        metrics = predictor.train(training_data)
        
        # Mostrar métricas
        print("\nMétricas de entrenamiento:")
        print(f"Score en entrenamiento: {metrics['train_score']:.4f}")
        print(f"Score en prueba: {metrics['test_score']:.4f}")
        
        # Mostrar importancia de características
        print("\nImportancia de características:")
        for feature, importance in metrics['feature_importance'].items():
            print(f"{feature}: {importance:.4f}")
        
        # Hacer predicción para el próximo día
        last_data = X.iloc[-1:].copy()
        prediction = predictor.predict(last_data)
        print(f"\nÚltimo precio real: ${data['Close'].iloc[-1]:.2f}")
        print(f"Predicción para el próximo día: ${prediction[0]:.2f}")
        
        # Guardar modelo
        predictor.save_model("btc_model")
        print("\nModelo guardado exitosamente")
        
    except Exception as e:
        print(f"\nError durante las pruebas: {str(e)}")

if __name__ == "__main__":
    test_model_with_real_data()