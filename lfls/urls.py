from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.main_view),
    # path('register/', views.register),
    # path('news/([0-9]+)/', views.news_id, name="news_detail"),
    # path('about/$', views.about)
    # path('about/$', views.about)
]
