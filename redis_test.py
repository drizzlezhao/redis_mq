import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host="127.0.0.1")
        self.chan_sub='104.5'
        self.chan_pub='104.5'

    def publish(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True

    def subscribe(self):
        pub=self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        print('pub',pub)
        pub.parse_response()
        return pub