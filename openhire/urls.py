from django.contrib import admin
from django.urls import path
from users.views import login_user
from employers.views import employers_home

urlpatterns = [
    path('admin/', admin.site.urls),
    #Users
    path('login/', login_user, name="login"),
    #Employers
    path('employers_home/', employers_home, name="employers_home"),
]
