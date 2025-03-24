import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_results():
    """Función para visualizar los resultados del modelo de predicción"""
    try:
        # Cargar resultados
        print("Cargando resultados...")
        results = pd.read_csv('prediction_results.csv')
        results['Fecha'] = pd.to_datetime(results['Fecha'])
        
        # 1. Gráfico de predicciones vs valores reales
        plt.figure(figsize=(15, 8))
        plt.plot(results['Fecha'], results['Precio Real'], 
                label='Real', linewidth=2, color='blue')
        plt.plot(results['Fecha'], results['Predicción'], 
                label='Predicción', linewidth=2, linestyle='--', color='red')
        plt.title('Precio de Bitcoin: Real vs Predicción', fontsize=14)
        plt.xlabel('Fecha', fontsize=12)
        plt.ylabel('Precio (USD)', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('btc_prediction_full.png', dpi=300)
        print("Gráfico de predicciones guardado como 'btc_prediction_full.png'")
        
        # 2. Distribución del error
        plt.figure(figsize=(10, 6))
        sns.histplot(data=results, x='Error', bins=50, color='skyblue')
        plt.title('Distribución del Error de Predicción', fontsize=14)
        plt.xlabel('Error (USD)', fontsize=12)
        plt.ylabel('Frecuencia', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('error_distribution.png', dpi=300)
        print("Histograma de errores guardado como 'error_distribution.png'")
        
        # 3. Estadísticas del error
        error_stats = {
            'Error Medio': results['Error'].mean(),
            'Error Mediano': results['Error'].median(),
            'Error Mínimo': results['Error'].min(),
            'Error Máximo': results['Error'].max(),
            'Desviación Estándar': results['Error'].std()
        }
        
        print("\nEstadísticas del Error:")
        print("-" * 40)
        for metric, value in error_stats.items():
            print(f"{metric:.<25} ${value:,.2f}")
        
        # 4. Métricas adicionales
        accuracy = (abs(results['Error']) < 1000).mean() * 100
        print(f"\nPrecisión (error < $1000): {accuracy:.2f}%")
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'prediction_results.csv'")
    except Exception as e:
        print(f"Error durante la visualización: {str(e)}")

if __name__ == "__main__":
    visualize_results()