
def simple_middleware(get_response):
    def middleware(request):
        print('before request')
        request = get_response(request)
        print('after request/response')
        return request
    return  middleware
