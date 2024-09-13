from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    path('get_user_by_email/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
    path('update_user/<str:email>/', views.update_user, name='update_user'),
    path('update_partial_user/<str:username>/', views.update_partial_user, name='update_partial_user'),
    path('delete_user/<str:username>/', views.delete_user, name='delete_user'),
]
