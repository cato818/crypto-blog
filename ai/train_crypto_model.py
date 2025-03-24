from data_loader import CryptoDataLoader
from model import CryptoPricePredictor
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def train_and_evaluate_model():
    """Entrena y evalúa el modelo de predicción"""
    print("Iniciando entrenamiento del modelo...")
    
    # Cargar datos
    loader = CryptoDataLoader('BTC-USD')
    data = loader.get_historical_data()
    
    if data is None or data.empty:
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
        importances = pd.Series(metrics['feature_importance'])
        importances.sort_values(ascending=False).plot(kind='bar')
        plt.title('Importancia de características')
        plt.tight_layout()
        plt.savefig('feature_importance.png')
        
        # Hacer predicción para el próximo día
        last_data = X.iloc[-1:].copy()
        prediction = predictor.predict(last_data)
        current_price = data['Close'].iloc[-1]
        
        print(f"\nÚltimo precio conocido: ${current_price:,.2f}")
        print(f"Predicción para el próximo día: ${prediction[0]:,.2f}")
        print(f"Cambio esperado: {((prediction[0] - current_price) / current_price * 100):,.2f}%")
        
        # Guardar modelo
        model_filename = f"btc_model_{datetime.now().strftime('%Y%m%d')}"
        predictor.save_model(model_filename)
        print(f"\nModelo guardado como: {model_filename}")
        
    except Exception as e:
        print(f"\nError durante el entrenamiento: {str(e)}")

if __name__ == "__main__":
    train_and_evaluate_model()