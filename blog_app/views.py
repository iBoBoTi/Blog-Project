from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView) 
from .models import Post
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class PostListView(ListView):
    model = Post 
    template_name = 'blog_app/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_app/post_new.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog_app/post_edit.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post-list')
