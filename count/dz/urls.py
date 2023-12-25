from django.urls import path

from .views import create, PostDetail, PostDelete

urlpatterns = [

    path('', create, name="load"),
    path('t/<int:pk>', PostDetail.as_view(), name="text"),
    path('t/<int:pk>/delete', PostDelete.as_view(), name='clear-memory'),
]