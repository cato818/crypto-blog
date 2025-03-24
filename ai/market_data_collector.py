import tweepy
import praw
import pandas as pd
from datetime import datetime
import time
import os
from dotenv import load_dotenv

class SocialDataCollector:
    def __init__(self):
        """Inicializa las conexiones a APIs de redes sociales"""
        load_dotenv()
        
        # Configuración Twitter/X
        self.twitter_client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
        )
        
        # Configuración Reddit
        self.reddit_client = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent='CryptoSentimentAnalyzer/1.0'
        )
        
    def get_twitter_data(self, query="bitcoin OR crypto", limit=100):
        """Obtiene tweets relacionados con criptomonedas"""
        try:
            tweets = self.twitter_client.search_recent_tweets(
                query=query,
                max_results=limit,
                tweet_fields=['created_at', 'public_metrics']
            )
            
            if not tweets.data:
                return []
                
            return [{
                'text': tweet.text,
                'created_at': tweet.created_at,
                'likes': tweet.public_metrics['like_count'],
                'retweets': tweet.public_metrics['retweet_count'],
                'source': 'Twitter'
            } for tweet in tweets.data]
            
        except Exception as e:
            print(f"Error obteniendo datos de Twitter: {e}")
            return []
            
    def get_reddit_data(self, subreddits=['Bitcoin', 'CryptoCurrency'], limit=100):
        """Obtiene posts de Reddit relacionados con crypto"""
        try:
            posts = []
            for subreddit_name in subreddits:
                subreddit = self.reddit_client.subreddit(subreddit_name)
                hot_posts = subreddit.hot(limit=limit//len(subreddits))
                
                for post in hot_posts:
                    posts.append({
                        'title': post.title,
                        'text': post.selftext,
                        'created_at': datetime.fromtimestamp(post.created_utc),
                        'score': post.score,
                        'comments': post.num_comments,
                        'source': f'Reddit/r/{subreddit_name}'
                    })
            
            return posts
            
        except Exception as e:
            print(f"Error obteniendo datos de Reddit: {e}")
            return []

def test_social_data():
    """Prueba la recolección de datos sociales"""
    collector = SocialDataCollector()
    
    print("\n📱 Obteniendo datos de redes sociales...")
    
    # Obtener datos de Twitter
    print("\n🐦 Buscando en Twitter...")
    tweets = collector.get_twitter_data(limit=10)
    if tweets:
        print(f"Se encontraron {len(tweets)} tweets")
        for tweet in tweets[:3]:
            print(f"\n• {tweet['text'][:100]}...")
            print(f"  👍 {tweet['likes']} | 🔁 {tweet['retweets']}")
    
    # Obtener datos de Reddit
    print("\n🎯 Buscando en Reddit...")
    reddit_posts = collector.get_reddit_data(limit=10)
    if reddit_posts:
        print(f"Se encontraron {len(reddit_posts)} posts")
        for post in reddit_posts[:3]:
            print(f"\n• {post['title']}")
            print(f"  ⬆️ {post['score']} | 💬 {post['comments']}")

if __name__ == "__main__":
    test_social_data()