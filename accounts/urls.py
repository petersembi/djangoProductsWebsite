# from django.urls import path, include
# from . import views

# urlpatterns = [
    
#     path('', views.register, name='register'),
   


# ]

from django.urls import path

from . import views

urlpatterns = [
    # path('', views.register, name ='register'),
    path("login/", views.login, name='login'),
    path('register/', views.register, name='register'),
]