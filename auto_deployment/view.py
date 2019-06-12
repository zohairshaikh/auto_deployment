from django.http import HttpResponse
from django.core.cache import cache
import random

def homeView(request):
    return HttpResponse('Welcome to Homepage')


def redisTest(request):

    cache.set('test', random.randint(0,100))

    return HttpResponse(cache.get('test'))
