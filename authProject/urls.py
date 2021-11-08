"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp                        import views

urlpatterns = [
    path('admin/',                                  admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/',                                TokenRefreshView.as_view()),
    path('user/',                                   views.UserCreateView.as_view()),
    path('user/superuser/',                         views.UserCreateSuperView.as_view()),
    path('user/<int:pk>/',                          views.UserDetailView.as_view()),
    path('habitacion/create/',                      views.HabitacionCreateView.as_view()),
    path('habitacion/detail/<int:user>/<int:pk>/',         views.HabitacionDetailView.as_view()),
    path('habitacion/detail/<int:user>/',                  views.HabitacionesView.as_view()),
    path('habitacion/remove/<int:user>/<int:pk>/',  views.HabitacionDelateView.as_view()),
    path('habitacion/update/<int:user>/<int:pk>/',  views.HabitacionUpdateView.as_view()),
    path('reserva/create/',                         views.ReservaCreateView.as_view()),
    path('reserva/detail/<int:user>/<int:pk>/',     views.ReservaDetailView.as_view()),
    path('reserva/detail/',                         views.ReservasView.as_view()),
    path('reserva/remove/<int:user>/<int:pk>/',     views.ReservaDelateView.as_view()),
    path('reserva/update/<int:user>/<int:pk>/',     views.ReservaUpdateView.as_view()),

]
