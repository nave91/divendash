from django.conf.urls import include, url
from django.contrib import admin

from django.communication.views import Verify

urlpatterns = [
    # Examples:
    # url(r'^$', 'divendash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'verify_url', Verify.as_view()),
]
