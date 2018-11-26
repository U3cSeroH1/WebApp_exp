from django.http import HttpResponse

from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader


from django.http import HttpResponseRedirect

from django.urls import reverse

from django.views import generic

from django.utils import timezone

from register.views import OnlyYouMixin

def index(request):
    return render(request, 'agrimap/ass.html')


class UserDetail(OnlyYouMixin, generic.DetailView):
    """ユーザーの詳細ページ"""
    #model = User
    template_name = 'agrimap/user_map.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く
