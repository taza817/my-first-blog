from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy



# def post_list(request) :
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:7]
#     return render(request, 'blog/post_list.html', {'posts':posts})

class PostList(ListView) :
    #template_name = 'blog/post_list.html'
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    # model = Post


# def post_detail(request, pk) :
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post':post})

class PostDetail(DetailView) :
    #template_name = 'blog/post_detail.html'
    model = Post


# def post_new(request) :
#     if request.method == "POST" :
#         form = PostForm(request.POST)
#         if form.is_valid() :
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)   #このpostは新しく作られたブログポスト
#     else :
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form':form})

class PostCreate(CreateView) :
    #template_name = 'blog/post_form.html
    model = Post
    fields = ['title', 'text', 'created_date', 'published_date']

    def get_success_url(self) :
        return reserve('post_detail', kwargs={'pk': self.object.pk})


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)     #urlsから追加のpkパラメータを渡し，編集したいPostモデルを取得する
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)     #フォームを作るときはポストをinstanceとして渡す（保存）
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)       #フォームを作るときはポストをinstanceとして渡す（編集のためにフォームを開く）
#     return render(request, 'blog/post_edit.html', {'form': form})

class PostUpdate(UpdateView) :
    template_name = 'blog/update_form.html'
    model = Post
    fields = ['title', 'text', 'created_date', 'published_date']

    def get_success_url(self) :
        return reserve('post_detail', kwargs={'pk': self.object.pk})


class PostDelete(DeleteView) :
    #template_name = 'blog/post_confirm_delete.thml'
    model = Post
    success_url = reverse_lazy('post_list')