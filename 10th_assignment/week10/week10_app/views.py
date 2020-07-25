from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.db.models import Q

from . models import Post

class index(ListView):
    template_name = 'index.html'
    context_object_name = 'post'
    def get_queryset(self):
        return Post.objects.all

class detail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

class base(DetailView):
    model = Post
    template_name = 'base.html'
    context_object_name = 'post'

class create(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'contents']
    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.author = self.request.user
        Post.save()
        return HttpResponseRedirect(self.request.POST.get('next', '/'))

def result(request):
    BlogPosts = Post.objects.all()
    query = request.GET.get('query', '')
    search_type = request.GET.get('search_type', '')
    if query:
        if search_type=="all":
            BlogPosts = BlogPosts.filter(Q(title__icontains=query)| Q(contents__icontains=query)).order_by('-time')

        elif search_type=="title":
            BlogPosts = BlogPosts.filter(Q(title__icontains=query)).order_by('-time')

        elif search_type=="contents":
            BlogPosts = BlogPosts.filter(Q(contents__icontains=query)).order_by('-time')

        else:
            BlogPosts = Post.objects.all()

    return render(request, 'result.html', {'BlogPosts':BlogPosts, 'query':query, 'search_type':search_type})