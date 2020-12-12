import time
import threading
from enum import Enum

FETCH_INTERVAL = 120


class Commands(Enum):
    start = '/start '
    subscribe = '/subscribe '
    unsubscribe = '/unsubscribe '
    subscriptions = '/subscriptions '


class StatusCodes(Enum):
    success = 200


class SetInterval:
    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__set)
        thread.start()

    def __set(self):
        next_time = time.time()+self.interval
        while not self.stopEvent.wait(next_time - time.time()):
            next_time += self.interval
            self.action()

    def cancel(self):
        self.stopEvent.set()
