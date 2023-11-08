from django.contrib import admin
from django.urls import path, re_path
#Import app's views
from users.views import login_user, logout_user, register_user
from employers.views import employers_home, employers_profile
from candidates.views import candidates_home, candidates_profile
# Serve Media Files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', register_user, name="register"),
    # Employers
    path('employers_home/', employers_home, name="employers_home"),
    path('employer_profile/<int:pk>', employers_profile, name="employers_profile"),
    # Candidates
    path('candidates_home/', candidates_home, name="candidates_home"),
    path('candidates_profile/<int:pk>', candidates_profile, name="candidates_profile"),
]

# Serve Media Files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

