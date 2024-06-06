from typing import Any
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import ListView,DetailView,TemplateView,FormView,View,CreateView
from .models import Post,Comment
from .forms import CommentForm
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class CommentGet(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin,FormView):
    model = Post
    form_class = CommentForm
    template_name  = "detail.html"

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        return super().post(request,*args,**kwargs)
    def form_valid(self,form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        post = self.get_object()
        return reverse("detail", kwargs={'pk':post.pk})


class PostDetailView(View):
    def get(self,request,*args,**kwargs):
        view = CommentGet.as_view()
        return view(request,*args,**kwargs,)
    
    def post(self,request,*args,**kwargs):
        view = CommentPost.as_view()
        return view(request,*args,**kwargs)



class AboutUsView(TemplateView):
    template_name = 'aboutus.html'