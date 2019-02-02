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
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm, MyPasswordChangeForm,
    MyPasswordResetForm, MySetPasswordForm
)

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse

from django.shortcuts import render

import json
import logging
import re

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, resolve_url
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm, MyPasswordChangeForm,
    MyPasswordResetForm, MySetPasswordForm
)

from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.utils import timezone

from django.http.response import JsonResponse
import os
module_dir = os.path.dirname(__file__) # views.pyのあるディレクトリを取得
json_path = os.path.join(module_dir, 'hoge.json')
from django.http import HttpResponse,Http404

import json
import logging
import re

from scraping.models import Tomorrow, Date

User = get_user_model()




class Top(generic.TemplateView, LoginView):
    form_class = LoginForm
    template_name = 'register/top.html'

    def get_context_data(self, **kwargs):
        # 継承元のメソッド呼び出し
        context = super().get_context_data(**kwargs)

        context["today"] = Tomorrow.objects.filter(target = Date.objects.get(pub_date= str(timezone.now().date())))
        
        context["tomorrow"] = Tomorrow.objects.filter(target = Date.objects.get(pub_date= str(timezone.now().date()+timezone.timedelta(days= 1 ))))
        return context


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LoginRequiredMixin, LogoutView, LoginView):
    """ログアウトページ"""
    form_class = LoginForm
    template_name = 'register/top.html'


class UserCreate(generic.CreateView):
    """ユーザー仮登録"""
    template_name = 'register/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """仮登録と本登録用メールの発行."""
        # 仮登録と本登録の切り替えは、is_active属性を使うと簡単です。
        # 退会処理も、is_activeをFalseにするだけにしておくと捗ります。
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject_template = get_template('register/mail_template/create/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('register/mail_template/create/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)
        return redirect('register:user_create_done')


class UserCreateDone(generic.TemplateView):
    """ユーザー仮登録したよ"""
    template_name = 'register/user_create_done.html'


class UserCreateComplete(generic.TemplateView):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'register/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """tokenが正しければ本登録."""
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoenNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # まだ仮登録で、他に問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スーパーユーザーだけユーザーページアクセスを許可する"""
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, generic.DetailView):
    """ユーザーの詳細ページ"""
    model = User
    template_name = 'register/user_detail.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    """ユーザー情報更新ページ"""
    model = User
    form_class = UserUpdateForm
    template_name = 'register/user_form.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く

    def get_success_url(self):
        return resolve_url('register:user_detail', pk=self.kwargs['pk'])


class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('register:password_change_done')
    template_name = 'register/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'register/password_change_done.html'


class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'register/mail_template/password_reset/subject.txt'
    email_template_name = 'register/mail_template/password_reset/message.txt'
    template_name = 'register/password_reset_form.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('register:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'register/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    form_class = MySetPasswordForm
    success_url = reverse_lazy('register:password_reset_complete')
    template_name = 'register/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'register/password_reset_complete.html'



def save_latlng(request):    # AJAXに答える関数
    print ("haro")

    if request.method == 'POST':
        txt = request.POST['lat'] # POSTデータを取得して
        txt2=request.POST['lng']
        txt3=request.POST['lng_s']
        txt4=request.POST['geo']
        print (request.get_full_path)
        print (txt3)
        txt3=txt3.strip("/")
        txt3=txt3.strip("user_update/")

        

        my_dict = {
           'lat':txt,
           'lng':txt2,
           'geo':txt4,
        }
        my_dict2 = json.dumps({'aaa':my_dict})
#        def test_func(self):
#            user = self.request.user
        #    return user.pk == self.kwargs['pk'] or user.is_superuser

#        return resolve_url('app:user_detail', pk=self.kwargs['pk'])
        U=User.objects.get(pk=txt3)
        U.example3=txt+":"+txt2
        U.lat=txt
        U.lng=txt2
        U.geo=txt4
        U.save()

        

        return HttpResponse(my_dict2,content_type='application/javascript')  # 返す。JSONはjavascript扱いなのか・・

    else:
        print("こんばんわ")
        raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも   



def pin(request, pk):

    
    User.objects.get(pk=pk)



    d={
        'lat' : User.objects.get(pk=pk).lat,
        'lng' : User.objects.get(pk=pk).lng,
        'User_p' : User.objects.get(pk=pk)
    }

    return render(request,'register/pin.html', d)

def pin_data(request):
    #print ("hro")





    #print(sorted(CHOICES2))


                    #print(vegi + "あ")
                    #print(U.pulldown + "あ")

    if request.method == 'POST':



        numbers=range(0,User.objects.last().id)

        

        print(User.objects.last().id)
        """
        for number in numbers:
            didict[number]={"lat":1,"lng":2,"num":number+10}
            
        dict2=json.dumps({'ccc':didict})  
        while True:
            i=i+1
            try:
                U=Userq.objects.get(pk=number)
                if()
                lat=U.lat
                lng=U.lng
                print(lat,lng)
            except:
                break
        """        
        didict={}
        for number in numbers:
            try:
                U=User.objects.get(pk=number+1)
                lat=U.lat
                lng=U.lng
                pulldown=U.pulldown

                didict[number+1]={"lat":lat,"lng":lng,"num":User.objects.last().id,"pulldown":pulldown}
                print(lat,lng,pulldown)
            except:
                didict[number+1]={"lat":-1,"lng":-1,"num":User.objects.last().id}
                print(number+1)
        
        dict2=json.dumps({'ccc':didict})  

        print("endgeiojgfeiojeoi")        
        """
        
        U=Userq.objects.get(pk=1)            
        lat=U.lat
        lng=U.lng
        print(lat,lng)       
        """
        
        

        
        return HttpResponse(dict2,content_type='application/javascript')  # 返す。JSONはjavascript扱いなのか・・

    else:
        print("こんばんわ")
        raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも  

@ensure_csrf_cookie
def view(request):
    pass
