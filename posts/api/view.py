from rest_framework import generics, permissions
from .serializers import UserSerializer,UserCreateSerializer, PostSerializer, PostCreateUpdateSerializer
from posts.models import User, Post

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You must be owner of this object'
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class UserListApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]

class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]
    lookup_field = 'username'

class PostListApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

class PostCreateApiView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateApiView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)





class UserPostList(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))