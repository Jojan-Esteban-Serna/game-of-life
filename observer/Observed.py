from typing import List

from observer.Observer import Observer


class Observed:
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()