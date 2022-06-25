from exceptions.custom_exception import InvlaidAlgorithmException
from ratelimiting_algos.base_rate_limiter import BaseRateLimiter
from ratelimiting_algos.sliding_window import SlidingWindowRateLimiter
from ratelimiting_algos.token_bucket_algo import TokenBucketAlgorithm


class RateLimitFactory:
    def get_ratelimiter(self, rate_limit_algo: str):
        if rate_limit_algo == 'SLIDING_WINDOW':
            return SlidingWindowRateLimiter
        elif rate_limit_algo == 'TOKEN_BUCKET':
            return TokenBucketAlgorithm
        else:
            raise InvlaidAlgorithmException()
