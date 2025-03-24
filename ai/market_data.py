import requests
import pandas as pd
from datetime import datetime, timedelta
import json
import os
from dotenv import load_dotenv

class MarketDataCollector:
    def __init__(self):
        load_dotenv()
        self.newsapi_key = os.getenv('NEWSAPI_KEY')
        self.fear_greed_url = "https://api.alternative.me/fng/"
        
    def get_crypto_news(self, days=7):
        """Obtiene noticias relacionadas con Bitcoin"""
        try:
            url = f"https://newsapi.org/v2/everything"
            params = {
                'q': 'bitcoin OR cryptocurrency',
                'language': 'en',
                'sortBy': 'publishedAt',
                'apiKey': self.newsapi_key,
                'from': (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()['articles']
            else:
                print(f"Error al obtener noticias: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error en get_crypto_news: {str(e)}")
            return None
            
    def get_fear_greed_index(self):
        """Obtiene el índice de miedo y codicia de crypto"""
        try:
            response = requests.get(self.fear_greed_url)
            if response.status_code == 200:
                return response.json()['data'][0]
            return None
        except Exception as e:
            print(f"Error al obtener índice de miedo y codicia: {str(e)}")
            return None
            
    def analyze_sentiment(self, news):
        """Analiza el sentimiento de las noticias"""
        if not news:
            return 0
            
        # Aquí podrías integrar un modelo de NLP más sofisticado
        positive_words = ['bull', 'bullish', 'gain', 'surge', 'rise', 'up']
        negative_words = ['bear', 'bearish', 'fall', 'drop', 'down', 'crash']
        
        sentiment_score = 0
        for article in news:
            title = article['title'].lower()
            sentiment_score += sum(1 for word in positive_words if word in title)
            sentiment_score -= sum(1 for word in negative_words if word in title)
            
        return sentiment_score / len(news)

    def get_market_indicators(self):
        """Recopila todos los indicadores de mercado"""
        news = self.get_crypto_news()
        sentiment = self.analyze_sentiment(news)
        fear_greed = self.get_fear_greed_index()
        
        return {
            'sentiment_score': sentiment,
            'fear_greed_index': fear_greed['value'] if fear_greed else None,
            'fear_greed_classification': fear_greed['value_classification'] if fear_greed else None,
            'news_count': len(news) if news else 0
        }