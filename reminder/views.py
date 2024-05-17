from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, TemplateView, FormView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LogoutView 
from .forms import Signup, TaskForm
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
#class LogoutTemplateView(TemplateView):
 #   template_name = 'logout.html'

class SignupFormView(FormView):
    template_name = 'signup.html'
    form_class = Signup
    success_url = reverse_lazy('accounts/')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class To_do_ListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'Task'

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_view.html'
    success_url = reverse_lazy('view')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())
    
    


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update.html'
    success_url =reverse_lazy ('view')


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url =reverse_lazy('view')
    task = Task()


class FormSuccesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Action successful")
    



def logout_view(request):
    logout(request)
    return redirect('/')