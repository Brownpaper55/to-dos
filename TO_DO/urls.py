"""
URL configuration for TO_DO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reminder import views, api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'),name='accounts'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.IndexView.as_view(), name='home'),
    path('SignUp/', views.SignupFormView.as_view(), name= 'signup'),
    path('view/', views.To_do_ListView.as_view(), name = 'view'),
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name = 'update_task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name = 'delete_task'),
    path('success/', views.FormSuccesView.as_view(), name= 'success'),
    path('api/all_tasks/',api_views.AllTasks.as_view(), name= 'all_tasks')
]
