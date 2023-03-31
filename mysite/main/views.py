from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.utils import timezone
from django.urls import reverse_lazy


class PostsListView(ListView):
    model = Post
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'home'
        context['Posts'] = Post.objects.filter(date__lte=timezone.now()).order_by('-date')
        return context






def about(request):
    context = {
        'title': 'about'
    }
    return render(request, 'main/about.html', context=context)


class ProjectsList(ListView):
    model = Post
    template_name = 'main/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Posts'] = Post.objects.filter(git__isnull=False)
        return context
    

def contacts(request):
    return render(request, 'main/contacts.html')


class ProjectDetail(DetailView):
    model = Post
    template_name = 'main/project_detail.html'
    slug_field = 'slug'






class AddMessage(CreateView):
    form_class = AddMessageForm
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('home')