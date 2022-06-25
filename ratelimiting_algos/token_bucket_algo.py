import threading
from datetime import datetime

from exceptions.custom_exception import TooManyRequestsException
from models.request import Request
from ratelimiting_algos.base_rate_limiter import BaseRateLimiter


class Bucket:
    def __init__(self, limit):
        self.limit = limit
        self.last_call_time = None


class TokenBucketAlgorithm(BaseRateLimiter):
    # assuming k token per minute
    def __init__(self,  resource, limit, token_gen_per_unit_time):
        super(TokenBucketAlgorithm, self).__init__(resource, limit)
        self.token_gen_per_unit_time = token_gen_per_unit_time
        self.user_bucket_map = dict()

    def apply(self, request: Request):
        now = datetime.now()
        lock = threading.Lock()
        if request.src in self.user_bucket_map:
            bucket = self.user_bucket_map[request.src]

            too_many_requests = False
            time_delta = now - bucket.last_call_time
            lock.acquire()
            if time_delta.total_seconds()//60 > 1:
                time_unit_passed = time_delta.total_seconds()//60
                tokens_added = time_unit_passed * self.token_gen_per_unit_time
                bucket.limit = min(self.limit, bucket.limit + tokens_added)
            if bucket.limit > 0:
                bucket.limit -= 1
            else:
                too_many_requests = True
            bucket.last_call_time = now
            lock.release()
            if too_many_requests:
                raise TooManyRequestsException()
        else:
            bucket = Bucket(self.limit)
            bucket.last_call_time = now
            lock.acquire()
            bucket.limit -= 1
            lock.release()
            self.user_bucket_map[request.src] = bucket

