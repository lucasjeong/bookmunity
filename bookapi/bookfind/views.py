from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
# Create your views here.

def index(request):
    return HttpResponse("For Test!")

def search(request):
    if request.method == 'GET':

        #config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())
        client_id = 'gqNyJgMrf19GMiiUJKQH'
        client_secret = 'MMQ26KysSJ'

        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/movie?query=" + encText
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            print(result)

            context = {
                'items': items
            }
            return render(request, 'bookfind/templates/templates.html', context = context)


# https://whatisthenext.tistory.com/137
# 참고 요
