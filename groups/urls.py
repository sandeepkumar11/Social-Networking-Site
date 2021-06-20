from django.urls import path

from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name="all"),
    path("new/", views.CreateGroup.as_view(), name="create"),
    path("posts/in/(?P<slug>[-\w]+)/",views.SingleGroup.as_view(),name="single"),
    path("join/(?P<slug>[-\w]+)/",views.JoinGroup.as_view(),name="join"),
    path("leave/(?P<slug>[-\w]+)/",views.LeaveGroup.as_view(),name="leave"),
]
