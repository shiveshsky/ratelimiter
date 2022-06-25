class Request:
    def __init__(self):
        self.__src: str = None  # source ip for each request
        self.__request_type: str = None
        self.__resource_url: str = None

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src_ip: str):
        self.__src = src_ip

    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, request_type):
        self.__request_type = request_type

    @property
    def resource_url(self):
        return self.__resource_url

    @resource_url.setter
    def resource_url(self, resource_url):
        self.__resource_url = resource_url
