from sdk.data.queue import Queue

a = Queue("redis://default:B106tQW3mK0DGORzEEcgkYUZiDgzOxlg@redis-15590.c13.us-east-1-3.ec2.cloud.redislabs.com:15590")

a.send(
    "test", "test_event", {
        "a": "b"
    }
)
