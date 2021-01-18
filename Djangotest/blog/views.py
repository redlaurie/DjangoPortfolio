from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView,UpdateView
from django.http import HttpResponse
from .models import Post,postImages
from django.contrib.auth.models import User
# Create your views here.
# python C:\Users\red-l\Django\Djangotest\manage.py path


def home(request):
    context = {'posts': Post.objects.all(),'title': 'Home'}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).ordery_by('-date_posted')

class PostDetailView(DetailView):
    print("this one 1")
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Post'] = Post.objects.filter(pk=self.object.pk)
        return context

def DetailView(request,pk):
    post = get_object_or_404(Post,id=pk)
    print(post)
    photos = postImages.objects.filter(post=post)
    print(photos)
    context = {'post':post,'photos':photos, 'title': post}
    print(context)
    return render(request, 'Blog/post_detail.html',context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
