from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import json
import urllib.request
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk = post_pk)

class UserCreateView(CreateView):
    template_name = 'registration/create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list')

class UserCreateDone(TemplateView):
    template_name = 'registration/create_done.html'

#책 검색
@csrf_exempt
def search(request):
    if request.method == 'GET':

        client_id = 'gqNyJgMrf19GMiiUJKQH'
        client_secret = 'MMQ26KysSJ'

        find = request.GET.get('find')
        encText = urllib.parse.quote("{}".format(find))
        url = "https://openapi.naver.com/v1/search/book?query=" + encText + "&display=100&start=1"

        book_api_request = urllib.request.Request(url)
        book_api_request.add_header("X-Naver-Client-Id", client_id)
        book_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(book_api_request)

        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')

            context = {
                'items': items
            }
            return render(request, 'bookfind/bookfind.html', context = context)
