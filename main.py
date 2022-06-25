
from time import sleep

from models.request import Request
from ratelimiting_algos.ratelimit_factory import RateLimitFactory

if __name__ == '__main__':

    request1 = Request()
    request1.request_type = 'GET'
    request1.resource_url = '/abc/def'
    request1.src = '127.0.0.1'

    request2 = Request()
    request2.request_type = 'GET'
    request2.resource_url = '/abc/def'
    request2.src = '127.0.0.1'

    request3 = Request()
    request3.request_type = 'GET'
    request3.resource_url = '/abc/def'
    request3.src = '127.0.0.1'

    request4 = Request()
    request4.request_type = 'GET'
    request4.resource_url = '/abc/def'
    request4.src = '127.0.0.1'

    token_bkt_algo = RateLimitFactory().get_ratelimiter('TOKEN_BUCKET')
    obj = token_bkt_algo('/abc/def', 2, 1)
    obj.apply(request1)
    obj.apply(request2)
    sleep(65)
    obj.apply(request3)
    # obj.apply(request4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
