from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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
