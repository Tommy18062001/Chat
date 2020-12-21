from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .forms import ChatForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat
from django.utils import timezone
from django.urls import reverse
# Create your views here.


class ChatCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:login'
    form_class = ChatForm
    model = Chat

    # what is this

    def form_valid(self, form):
        my_message = form.save(commit=False)
        my_message.user = self.request.user
        my_message.save()
        return super().form_valid(form)


class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    context_object_name = "mess"

    def get_queryset(self):
        return Chat.objects.filter(posted_at__lte=timezone.now()).order_by('posted_at')

