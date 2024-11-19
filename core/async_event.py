
import asyncio

class AsyncEvent:
    def __init__(self):
        self._subscribers = []

    # Подписаться на событие (поддерживаются как асинхронные, так и синхронные функции)
    def subscribe(self, callback):
        self._subscribers.append(callback)

    # Вызвать событие
    def trigger(self, *args, **kwargs):
        for callback in self._subscribers:
            if asyncio.iscoroutinefunction(callback):
                asyncio.run(callback(*args, **kwargs))  # Асинхронный обработчик
            else:
                callback(*args, **kwargs)  # Синхронный обработчик
