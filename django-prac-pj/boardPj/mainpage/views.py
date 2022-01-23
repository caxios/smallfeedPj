from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Feed


def home(request):
    context = {
        'feeds': Feed.objects.all()
    }
    return render(request, 'mainpage/home.html', context)


class FeedListView(ListView):
    model = Feed
    template_name = 'mainpage/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Feeds'
    ordering = ['-date_Feeded']


class FeedDetailView(DetailView):
    model = Feed


class FeedCreateView(LoginRequiredMixin, CreateView):
    model = Feed
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FeedUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Feed
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Feed = self.get_object()
        if self.request.user == Feed.author:
            return True
        return False


class FeedDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Feed
    success_url = '/'

    def test_func(self):
        Feed = self.get_object()
        if self.request.user == Feed.author:
            return True
        return False