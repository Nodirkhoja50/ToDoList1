from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,CustomLogoutView,RegisterPage

urlpatterns = [
    path('',TaskList.as_view(),name = 'task'),
    path('task/<int:pk>/',TaskDetail.as_view(),name = 'task-detail'),
    path('task-create/',TaskCreate.as_view(),name = 'task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name = 'task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name = 'task-delete'),

    path('login-user/',CustomLoginView.as_view(),name = 'login-user'),
    path('login-out/',CustomLogoutView.as_view(),name = 'login-out'),
    path("register/",RegisterPage.as_view(),name = 'register')
]