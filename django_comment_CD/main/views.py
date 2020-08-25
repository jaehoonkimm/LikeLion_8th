from django.views import generic
from django.views.generic.edit import UpdateView

from .models import Post,Comment
from .forms import CommentForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from django.contrib import messages

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    def get_queryset(self): #ListView에서 사용-표시 하려는 개체 목록을 결정한다. 
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post #queryset = Post.objects.all()이랑 같은 기능
    template_name = 'detail.html'
    context_object_name='ppost'
    def get_context_data(self, **kwargs):
        context_data =  super(DetailView, self).get_context_data(**kwargs)
        context_data['form'] = CommentForm()
        context_data['comments'] = self.object.comment_set.all()
        return context_data

class UpdateView(generic.DetailView):
    model = Post #queryset = Post.objects.all()이랑 같은 기능
    template_name = 'update.html'
    context_object_name='ppost'
    def get_context_data(self, **kwargs):
        context_data =  super(DetailView, self).get_context_data(**kwargs)
        context_data['form'] = CommentForm()
        context_data['comments'] = self.object.comment_set.all()
        return context_data


def comment_create(request, post_id):
    if not request.user.is_anonymous:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
        else:
            messages.info(request, "올바르지 않은 댓글 형식입니다.")
    else:
        messages.info(request, "로그인이 필요합니다.")
    return HttpResponseRedirect(reverse('detail', args=(post_id,)))

def comment_delete(request, post_id, comment_id):
    comment_value = Comment.objects.get(pk=comment_id)
    if request.user == comment_value.author:
        comment_value.delete()
        return HttpResponseRedirect(reverse('detail', args=(post_id,)))
    else:
        messages.info(request, "댓글 삭제 권한이 없습니다.")
        return HttpResponseRedirect(reverse('detail', args=(post_id,)))

def comment_update(request, post_id, comment_id):
    comment_value = Comment.objects.get(pk=comment_id)
    if comment_value.author == request.user:
        comment_form = CommentForm(instance=comment_value)
        if request.method == "POST":
            updated_form = CommentForm(request.POST, instance = comment_value)
            if updated_form.is_valid():
                updated_form.save()
                return HttpResponseRedirect(reverse('detail',args=(post_id,)))
        return render(request,'update.html', {'comment_form':comment_form})
    else:
        messages.info(request,"댓글 수정 권한이 없습니다.")
        return HttpResponseRedirect(reverse('detail',args=(post_id,)))