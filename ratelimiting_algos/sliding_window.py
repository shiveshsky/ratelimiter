from collections import defaultdict, deque
from datetime import datetime

from exceptions.custom_exception import TooManyRequestsException
from models.request import Request
from ratelimiting_algos.base_rate_limiter import BaseRateLimiter


class SlidingWindowRateLimiter(BaseRateLimiter):
    def __init__(self, resource, limit, time_diff):
        super(SlidingWindowRateLimiter, self).__init__(resource, limit)
        self.time_diff = time_diff
        self.client_window_map = defaultdict(deque)

    def apply(self, request: Request):
        now = datetime.now()
        if request.resource_url == self.resource:
            if request.src in self.client_window_map:
                if len(self.client_window_map[request.src]) <= self.limit:
                    self.client_window_map[request.src].append(now)
                else:
                    while len(self.client_window_map[request.src]) > 0 and now - self.client_window_map[request.src][0] > self.time_diff:
                        self.client_window_map[request.src].popleft()
                    if len(self.client_window_map[request.src]) <= self.limit:
                        self.client_window_map[request.src].append(now)
                    else:
                        raise TooManyRequestsException()
            else:
                self.client_window_map[request.src].append(now)
