from django.conf import settings
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


CHOICES = (
    ('', '選択肢から選んでください'),
    ('ほうれん草', 'ほうれん草'),
    ('白菜', '白菜'),
    ('トマト', 'トマト'),
    ('たまねぎ', '玉ねぎ'),
    ('ナス', 'ナス'),
    ('ネギ', 'ネギ'),
    ('ジャガイモ', 'ジャガイモ'),
    ('きのこ', 'きのこ'),
    ('にんじん', 'にんじん'),
    ('だいこん', 'だいこん'),
    ('かぼちゃ', 'かぼちゃ'),
    ('きゅうり', 'きゅうり'),
    ('ブロッコリー', 'ブロッコリー'),
    ('ピーマン', 'ピーマン'),
    ('キャベツ', 'キャベツ'),
    ('米', '米'),
    ('麦', '麦'),
    ('イチゴ', 'イチゴ'),
    ('カボス', 'カボス'),
    ('みかん', 'みかん'),
    ('梨', '梨'),
    ('ぶどう', 'ぶどう'),
    ('キウイ', 'キウイ'),
    ('その他', 'その他'),
)


CHOICES2 = ['ほうれん草','白菜','トマト', 'たまねぎ', 
               'ナス', 'ネギ', 'ジャガイモ', 'きのこ', 'にんじん', 'だいこん', 'かぼちゃ', 'きゅうり', 'ブロッコリー', 'ピーマン', 'キャベツ', '米', 'イチゴ', 'カボス', 'みかん', '梨', 'ぶどう', 'キウイ', 'その他', 

]

# registerのUserモデルを使う場合だけ、登録する

class UserManager(BaseUserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given username, email, and
        password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル

    usernameを使わず、emailアドレスをユーザー名として使うようにしています。
    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    example1=models.CharField(_('example1'),max_length=150,blank=True)
    example2=models.CharField(_('example2'),max_length=150,blank=True)
    example3=models.CharField(_('example3'),max_length=150,blank=True)
    pulldown = models.CharField(_('pulldown'), choices=CHOICES,max_length=150,blank=True)
    lat=models.CharField(_('lat'),max_length=150,blank=True)
    lng=models.CharField(_('lng'),max_length=150,blank=True)
    geo=models.CharField(_('geo'),max_length=150,blank=True)

    HN = models.CharField(_('ユーザ名'),max_length=150)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email

