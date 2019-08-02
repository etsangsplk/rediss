import redis
import os


class RedisLogger():
    """
    Handle requests to redis.

    Set env vars REDIS_HOST, REDIS_PORT and REDIS_PASSWORD to connect.
    """
    host = os.getenv('REDIS_HOST')
    port = os.getenv('REDIS_PORT')
    password = os.getenv('REDIS_PASSWORD')
    r = redis.Redis(host=host, port=port, password=password)

    def set(self, k: str, v: str) -> None:
        """
        sets the key k with the value v in redis
        """
        self.r.set(k, v)

    def get(self, k: str) -> str:
        """
        get's the value for key k from redis
        """
        res = self.r.get(k)
        if res is not None:
            return res.decode('utf-8')
        return None

    def delete(self, k: str) -> list:
        """
        delete key and value pair for key k
        """
        self.r.delete(k)

    def keys(self, pattern: str) -> list:
        """
        get all keys for pattern
        """
        res = self.r.keys(pattern=pattern)
        return [x.decode('utf-8') for x in res]