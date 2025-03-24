from dotenv import load_dotenv
import os
import pathlib

def test_env():
    """Verifica la configuración del archivo .env y la API key"""
    # Verificar existencia del archivo
    env_path = pathlib.Path('d:/crypto-blog/ai/.env')
    if not env_path.exists():
        print("✗ Error: Archivo .env no encontrado")
        print(f"  Ruta buscada: {env_path.absolute()}")
        return

    # Cargar variables de entorno
    load_dotenv()
    
    # Verificar API key
    api_key = os.getenv('NEWSAPI_KEY')
    
    if api_key:
        print("✓ Archivo .env encontrado")
        print("✓ API key cargada correctamente")
        print(f"✓ Longitud de la API key: {len(api_key)} caracteres")
        print(f"✓ Primeros 5 caracteres: {api_key[:5]}...")
    else:
        print("✗ Error: API key no encontrada en .env")
        print("  El archivo debe contener exactamente:")
        print("  NEWSAPI_KEY=6d62c387d9544d328543318d60f0e46f")
        print("  Sin espacios alrededor del =")

if __name__ == "__main__":
    test_env()