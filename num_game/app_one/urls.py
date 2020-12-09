from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('guess', views.guess),
    path('clear', views.clear_session),
    path('user/create', views.create),
    path('leaderboards', views.leaderboards),
    path('delete/<int:id>', views.destroy
    )
]