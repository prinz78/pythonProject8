from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView,
                                       UpdateView,
                                       DeleteView)
from .models import Article
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_details.html'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    fields = ('title','body',)
    template_name = 'article_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)