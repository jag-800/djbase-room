from django.urls import path
from . import views
from .views import TodoTop, TodoDetail, TodoList, TodoCreate, TodoUpdate, TodoDelete

# app_name = 'todo'

urlpatterns = [
  path("", TodoTop.as_view(), name="top"),
  path("todo", TodoList.as_view(), name="list"),
  path("todo/detail/<int:pk>", TodoDetail.as_view(), name="detail"),
  path("todo/create/", TodoCreate.as_view(), name="create"),
  path("todo/update/<int:pk>", TodoUpdate.as_view(), name="update"),
  path("todo/delete/<int:pk>", TodoDelete.as_view(), name="delete"),
  path('user_create/', views.UserCreate.as_view(), name='user_create'),
  path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
  path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
  path('login/', views.Login.as_view(), name='login'),
  path('todo/logout/', views.Logout.as_view(), name='logout')
]

