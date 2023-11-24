from django.contrib import admin
from django.urls import path, re_path
# Import app's views
from users.views import login_user, logout_user, register_user
from employers.views import employers_home, employers_profile
from candidates.views import candidates_home, candidates_profile, search_job_offers
from job_offers.views import post_offer
from job_application.views import apply_for_job, job_offer_detail
# Serve Media Files
from django.conf import settings
from django.conf.urls.static import static
#

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
    path('search/', search_job_offers, name='search_job_offers'),
    # Job Applications
    path('job/<int:job_offer_id>/', job_offer_detail, name='job_offer_detail'),
    path('job/<int:job_offer_id>/apply/', apply_for_job, name='apply_for_job'),
    #Job Offers
    path('post_offer/', post_offer, name="post_offer"),
]

# Serve Media Files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)