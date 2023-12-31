from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login/',include('authorisation.urls'),name='login_route')
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup_user,name='signup'),
]