from flask_caching import Cache
import os

# configuration
config = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_REDIS_HOST": os.getenv("CACHE_REDIS_HOST"),
    "CACHE_REDIS_URL": os.getenv("CACHE_REDIS_URL"),
}

cache = Cache(config=config)
