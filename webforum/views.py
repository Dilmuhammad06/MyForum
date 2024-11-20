from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Tread, Post
from .forms import PostsForm


class IndexView(View):
    def get(self,request):
        categories = Category.objects.all()
        return render(request,'index.html',{"categories":categories})

class TreadsView(View):
    def get(self,request,category_id):
        cat = Category.objects.get(id=category_id)
        treads = Tread.objects.filter(category=cat)
        return render(request,'treads.html',{"category":cat,"treads":treads})

class PostsView(View):
    def get(self,request,tread_id):
        tread = Tread.objects.get(id=tread_id)
        posts = Post.objects.filter(tread=tread)
        form = PostsForm()
        return render(request,'posts.html',{"tread":tread,"posts":posts,"form":form})

    def post(self,request,tread_id):
        tread = Tread.objects.get(id=tread_id)
        posts = Post.objects.filter(tread=tread)
        form = PostsForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.tread = tread
            new_form.save()
            return redirect('posts', tread_id=tread_id)
        return render(request,'posts.html',{"tread":tread,"posts":posts,"form":form})
