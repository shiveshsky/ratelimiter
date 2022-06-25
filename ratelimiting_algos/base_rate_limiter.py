from abc import ABC, abstractmethod

from models.request import Request


class BaseRateLimiter(ABC):
    def __init__(self, resource, limit):
        self.resource = resource
        self.limit = limit

    @abstractmethod
    def apply(self, request: Request):
        pass
