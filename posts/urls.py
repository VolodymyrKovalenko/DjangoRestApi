from django.conf.urls import url, include
from rest_framework import routers
from posts.api.urls import user_urls, post_urls



urlpatterns = [
    url(r'^users/', include(user_urls)),
    url(r'^posts/', include(post_urls)),
]