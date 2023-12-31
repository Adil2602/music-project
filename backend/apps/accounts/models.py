from django.db import models

# Create your models here.
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from ..music.models import Music

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

MALE_CHOICES = (
    ('Мужчина','Мужчина'),
    ('Женщина','Женщина'),
    ('Другое','Другое'),
)

class User(AbstractUser):
    username = models.CharField('Имя пользователя',
                                max_length=10,
                                unique=True)
    email = models.EmailField('Электронная почта',
                              max_length=30,
                              unique=True)
    sex = models.CharField('Пол',
                           choices=MALE_CHOICES,
                           default='None')
    age = models.DateTimeField('Дата рождения',
                               null=True,
                               blank=True)
    phone = models.CharField('Телефон',
                             max_length=10,
                             null=True,
                             blank=True)
    created = models.DateTimeField('Дата создания аккаунта',
                                   auto_now_add=True)
    avatar = models.ImageField('фото',
                               upload_to='media/images/',
                               null=True,
                               blank=True)
    favorite_song = models.ManyToManyField(Music,
                                           verbose_name='Избранные песни',
                                           related_name='favorite_song',)

    objects = UserManager()
