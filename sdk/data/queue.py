import json
import time

import redis


class Queue:
    def __init__(self, redis_uri: str):
        """
        Example redis uri: redis://user:pwd@host:port
        @param redis_uri:
        """

        self.redis_uri = redis_uri
        self.redis = redis.from_url(redis_uri)
        self.pubsub = self.redis.pubsub()

    def send(self, channel: str, event_name: str, data: dict) -> None:
        """
        Send message to a given channel
        @param channel:
        @param event_name:
        @param data:
        @return:
        """
        data = {
            "event": str(event_name),
            "data": data,
            "createdAt": int(time.time())

        }
        self.redis.publish(
            channel,
            json.dumps(data).encode("utf-8"),
        )

    def receive(self, callback, channel: str, sleep: int = 0.01) -> dict:
        """
        I believe this only works for one channel to subscribe to
        @param callback:
        @param channel:
        @param sleep:
        @return:
        """
        self.pubsub.subscribe(channel)
        while True:
            msg = self.pubsub.get_message()
            if msg:
                if msg["data"] != 1:
                    callback(json.loads(msg["data"].decode("utf-8")))
            time.sleep(sleep)
