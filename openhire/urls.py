from django.contrib import admin
from django.urls import path
from users.views import login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    #users
    path('login/', login_user, name="login"),
]
