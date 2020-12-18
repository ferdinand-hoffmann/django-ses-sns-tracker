from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from django_ses.views import handle_bounce


app_name = 'ses_sns_tracker'

urlpatterns = [
    url(r'^bounce/$', csrf_exempt(handle_bounce)),
]