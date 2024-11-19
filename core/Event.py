class Event:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)