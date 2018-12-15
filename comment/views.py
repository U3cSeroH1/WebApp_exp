from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from .models import Post, Comment, Reply
 
 
class PostListView(generic.ListView):
    """/ でアクセス記事一覧."""
    model = Post
 
 
class PostDetailView(generic.DetailView):
    """/detail/post_pk でアクセス。記事詳細."""
    model = Post
 
 
class CommentView(generic.CreateView):
    """/comment/post_pk コメント投稿."""
    model = Comment
    fields = ('name', 'text')
    template_name = 'app/comment_form.html'
 
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
 
        # 紐づく記事を設定する
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
 
        # 記事詳細にリダイレクト
        return redirect('post_detail', pk=post_pk)
 
 
class ReplyView(generic.CreateView):
    """/reply/comment_pk 返信コメント投稿."""
    model = Reply
    fields = ('name', 'text')
    template_name = 'app/comment_form.html'
 
    def form_valid(self, form):
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
 
        # 紐づくコメントを設定する
        reply = form.save(commit=False)
        reply.target = comment
        reply.save()
 
        # 記事詳細にリダイレクト
        return redirect('post_detail', pk=comment.target.pk)