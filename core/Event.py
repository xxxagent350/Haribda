import asyncio

class Event:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            asyncio.create_task(handler(*args, **kwargs))