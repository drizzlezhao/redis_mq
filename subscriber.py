from redis_test import RedisHelper
import redis
from concurrent.futures import ThreadPoolExecutor
obj1 = RedisHelper()
redis_sub = obj.subscribe()
r = redis.Redis(host="127.0.0.1",port=6379,db=1)
thread_pool = ThreadPoolExecutor(5)
def push(msg):
    r.lpush('adoing',msg)
    print("doing")

while True:
    msg = redis_sub.parse_response()
    print(msg)
    thread_pool.submit(push,msg[2])
    print('success')
