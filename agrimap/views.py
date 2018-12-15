from django.http import HttpResponse

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

from comment.models import Post, Comment, Reply






class DetailView(OnlyYouMixin, generic.TemplateView):
    """ユーザーの詳細ページ"""
    #model = User
    template_name = 'agrimap/detail.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く
