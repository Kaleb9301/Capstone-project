from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'', views.MenuItemView)


urlpatterns = [
    path('booking/', views.bookingview.as_view()),
    path('menu/', include(router.urls)),
    path('menu/<int:pk>', views.SingleMenuItem.as_view()),
    path('menu-items/', include(router.urls)),
    path('menu-items/<int:pk>', views.SingleMenuItem.as_view()),
    path('api-token-auth', obtain_auth_token),
    path('message/', views.msg),
]