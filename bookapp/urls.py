from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:pk>/edit',Update.as_view(),name='post_edit'),
    path('',ListView.as_view(),name='home'),
    path('post/<int:pk>/',DetailView.as_view(),name='post'),
    path('post/new/',Create.as_view(),name='new'),
    path('post/<int:pk>/delete',Delete.as_view(),name='delete')   
]
