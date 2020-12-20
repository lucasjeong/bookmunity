CLIENT_ID = 'gqNyJgMrf19GMiiUJKQH'

CLIENT_SECRET = 'MMQ26KysSJ'

def search_book(query):

    from urllib.request import Request, urlopen

    from urllib.parse import urlencode, quote

    import json

    request = Request('https://openapi.naver.com/v1/search/book?query='+quote(query))

    request.add_header('X-Naver-Client-Id', CLIENT_ID)

    request.add_header('X-Naver-Client-Secret', CLIENT_SECRET)


    response = urlopen(request).read().decode('utf-8')

    search_result = json.loads(response)

    return search_result



if __name__ == "__main__":

    print(search_book('리버풀'))
