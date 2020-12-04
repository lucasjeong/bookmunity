from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("For Test!")

# https://whatisthenext.tistory.com/137
# 참고 요
