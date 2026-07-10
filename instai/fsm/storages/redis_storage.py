from redis.asyncio.connection import ConnectionPool
from redis.asyncio import Redis

class RedisStorage:
    def __init__(self, url: str, **kwargs):
        pool = ConnectionPool.from_url(url=url, **kwargs)
        self.client = Redis.from_pool(pool)
