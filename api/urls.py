from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, TaskListView, TaskRetrieveView,\
    PostListView, PostRetrieveView


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('blog-list/', PostListView.as_view(), name='blog-list'),
    path('blog-detail/<str:pk>/', PostRetrieveView.as_view(), name='blogs-detail'),
    path('task-list/', TaskListView.as_view(), name='task-list'),
    path('task-detail/<str:pk>/', TaskRetrieveView.as_view(), name='task-detail'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
