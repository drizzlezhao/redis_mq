from redis_test import RedisHelper
import redis
r = redis.Redis(host="127.0.0.1",port=6379,db=1)
obj = RedisHelper()
def rpop():
    msg = r.rpop('pending')
    print(msg)
    return msg
obj.publish(rpop())