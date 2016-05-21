# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.

def home_page(request):
    blog_name = "myblog"
    article_lists = Article.objects.all().order_by('-create_at')
    article_lists = [article_list.data for article_list in article_lists]

    data = {
        'blog_name': blog_name,
        'article_lists': article_lists,
    }
    return render(request, 'index.html', data)


def blog_fullwidth(request):
    blog_name = "myblog"
    article_lists = Article.objects.all().order_by('-create_at')
    article_lists = [article_list.data for article_list in article_lists]

    data = {
        'blog_name': blog_name,
        'article_lists': article_lists,
    }
    return render(request, 'full-width.html', data)


def article_view(request, pk):
    # title = request.GET.get('title', '')
    # title = u'这里是文章的题目'   # test

    article = get_object_or_404(Article, pk=pk).data

    return render(request, 'single.html', article)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def test(request):
    message = ['this a message']
    data = {
        'messages': message,
    }
    return render(request, 'test.html', data)