from django.http import HttpResponse


import comment


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

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

from django.core.mail import send_mail

from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, resolve_url
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import generic


User = get_user_model()


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
