

from queue import Queue

class Buffer:
    def __init__(self):
        self.queue = Queue(maxsize=10)

    def produce(self, item):
        self.queue.put(item)

    def consume(self):
        return self.queue.get()