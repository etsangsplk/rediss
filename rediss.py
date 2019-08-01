import redis
import os

class RedisLogger():
    host = os.getenv('REDIS_HOST')
    port = os.getenv('REDIS_PORT'),
    password = os.getenv('REDIS_PASSWORD')
    r = redis.Redis(host=host, port=port, password=password)

    def set(self, k, v): 
        self.r.set(k, v)

    def get(self, k): 
        res = self.r.get(k)
        if res is not None:
            return res.decode('utf-8')
        return None

    def delete(self, k): 
        self.r.delete(k)

    def keys(self, pattern):
        res = self.r.keys(pattern=pattern)
        return [x.decode('utf-8') for x in res]