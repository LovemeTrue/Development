import random
import threading
import time
from collections import defaultdict
from pprint import pprint
from typing import Callable

class SomethingWithEvent:
    """Simple example"""

    def __init__(self):
        self._events = defaultdict(dict)
        self._lock = threading.Lock()

    def add_handler(self, f: Callable, v: int):
        with self._lock:
            self._events[f][v] = v

    @property
    def get_events(self):
        return self._events



def worker(event_thread: SomethingWithEvent, f: Callable, v: int):
    pause = random.randint(1,2)
    time.sleep(pause)
    event_thread.add_handler(f, v)

event_thread = SomethingWithEvent()
for i in range(10):
    t = threading.Thread(target = worker, args = (event_thread, lamda x:x=x+1, i))
    t.start()


main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

pprint(event_thread.get_events)
"""
defaultdict(<class 'dict'>,
            {<function some_func at 0x7ff70d39c0d0>: {0: 0,
                                                      1: 1,
                                                      2: 2,
                                                      3: 3,
                                                      4: 4,
                                                      5: 5,
                                                      6: 6,
                                                      7: 7,
                                                      8: 8,
                                                      9: 9}})
"""