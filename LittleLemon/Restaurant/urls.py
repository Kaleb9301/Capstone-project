from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.MenuItemView)


urlpatterns = [
    path('booking/', views.bookingview.as_view()),
    path('menu/', include(router.urls)),
    path('menu/<int:pk>', views.SingleMenuItem.as_view())
]