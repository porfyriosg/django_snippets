from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from home.views import Home; app1=Home()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView, name='logout'),
    path('', app1.main, name='home'),
]
