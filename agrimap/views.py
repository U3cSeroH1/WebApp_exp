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

from .models import latlng

from .forms import latlngForm

User = get_user_model()


class DetailView(OnlyYouMixin, generic.DetailView):
    """ユーザーの詳細ページ"""
    model = User

    #form_class = latlngForm


    template_name = 'agrimap/detail.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く


    