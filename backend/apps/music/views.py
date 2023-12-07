from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Singer, Group, Music
# Create your views here.


class SingersView(ListView):
    model = Singer
    template_name = 'singers.html'
    context_object_name = 'singers'
    queryset = Singer.objects.all()

class GroupsView(ListView):
    model = Group
    template_name = 'groups.html'
    context_object_name = 'groups'
    queryset = Group.objects.all()

class GroupDetailView(DetailView):
    model = Group
    template_name = 'group_detail.html'
    context_object_name = 'group'
    queryset = Group.objects.all()

class SingerDetailView(DetailView):
    model = Singer
    template_name = 'singer_detail.html'
    context_object_name = 'singer'
    queryset = Singer.objects.all()

class MusicView(ListView):
    model = Music
    template_name = 'music_list.html'
    context_object_name = 'musics'
    queryset = Music.objects.all()

class MusicDetailView(DetailView):
    model = Music
    template_name = 'music_detail.html'
    context_object_name = 'music'
    queryset = Music.objects.all()


