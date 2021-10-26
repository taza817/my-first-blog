from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request) :
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request) :
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)   #このpostは新しく作られたブログポスト
    else :
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)     #urlsから追加のpkパラメータを渡し，編集したいPostモデルを取得する
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)     #フォームを作るときはポストをinstanceとして渡す（保存）
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)       #フォームを作るときはポストをinstanceとして渡す（編集のためにフォームを開く）
    return render(request, 'blog/post_edit.html', {'form': form})