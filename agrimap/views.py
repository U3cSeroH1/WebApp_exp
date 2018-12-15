from django.http import HttpResponse
from register.models import User

import comment
#from register.models import User
from polls.models import Question

from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader


from django.http import HttpResponseRedirect

from django.urls import reverse

from django.views import generic

from django.utils import timezone

from register.views import OnlyYouMixin

from comment.views import *







class DetailView(OnlyYouMixin, generic.DetailView):
    """ユーザーの詳細ページ"""
    model = User



    template_name = 'agrimap/detail.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く


    fields = ('name', 'text')

 
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
 
        # 紐づく記事を設定する
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
 
        # 記事詳細にリダイレクト
        return redirect('post_detail', pk=post_pk)
