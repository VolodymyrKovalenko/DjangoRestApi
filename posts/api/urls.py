from django.conf.urls import url, include

from .view import UserListApiView, UserDetailApiView, UserPostList, UserCreateApiView
from .view import PostListApiView, PostDetailApiView, PostUpdateApiView,PostCreateApiView



user_urls = [
    url(r'^register/$', UserCreateApiView.as_view(), name='register'),
    url(r'^(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='user-post-list'),
    url(r'^(?P<username>[0-9a-zA-Z_-]+)$', UserDetailApiView.as_view(), name='user-detail'),
    url(r'^$', UserListApiView.as_view(), name='user-list')
]

post_urls = [
    url(r'^(?P<pk>\d+)$', PostDetailApiView.as_view(), name='post-detail'),
    url(r'^$', PostListApiView.as_view(), name='post-list'),
    url(r'^create/$', PostCreateApiView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateApiView.as_view(), name='update')
]


