import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://clustercfg.redistest.cske7d.use1.cache.amazonaws.com:6379')
