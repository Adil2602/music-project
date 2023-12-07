from django.db import models

# Create your models here.


class Singer(models.Model):
    first_name = models.CharField('Имя исполнителя',
                                  max_length=100,
                                  blank=True,
                                  null=True)
    last_name = models.CharField('Фамилия исполнителя',
                                 max_length=100,
                                 blank=True,
                                 null=True)
    nickname = models.CharField('Псевдоним',
                                max_length=100,
                                blank=True,
                                null=True)
    photo = models.ImageField('Photo',
                              upload_to='singers/')
    biography = models.TextField('Биография')
    # music = models.ManyToManyField('Music', verbose_name='Музыка исполнителя', related_name='singer_music')
    # group = models.ManyToManyField('Group', verbose_name='Группа', related_name='singer_group')
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.nickname

class Group(models.Model):
    group_name = models.CharField('Название группы',
                                  max_length=100)
    photo = models.ImageField('Photo',
                              upload_to='groups/')
    biography = models.TextField('Биография')
    created_date = models.DateField('Дата создания группы')
    singer = models.ManyToManyField(Singer,
                                    verbose_name='Исполнитель',
                                    related_name='singer_group',)
    # music = models.ManyToManyField('Music', verbose_name='Музыка исполнителя', related_name='singer_music')
    # group = models.ManyToManyField('Group', verbose_name='Группа', related_name='singer_group')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.group_name



class Genre(models.Model):
    name = models.CharField('Жанр',
                            max_length=50,
                            unique=True)
    slug = models.SlugField('Слаг',
                            max_length=50,
                            unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.CharField('Название музыки', max_length=100)
    singer = models.ManyToManyField(Singer,
                                    verbose_name='Исполнитель',
                                    related_name='singer_music',)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete=models.CASCADE,
                              related_name='music_group',
                              blank=True,
                              null=True)
    public_date = models.DateField('Дата выпуска песни')
    text_song = models.TextField('Текст песни',
                                 blank=True,
                                 null=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр песни',
                                   related_name='music_genre')
    music = models.FileField('Музыка',
                             upload_to='music/')

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'
        ordering = ['-public_date']

    def __str__(self):
        return self.title

