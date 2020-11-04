from django.urls import path, re_path
from Profile import views

urlpatterns=[
    re_path(r'^profileModel_url',views.ProfileModelView.as_view()),
    re_path(r'^profileModel_users',views.ProfileUserView.as_view()),
    re_path(r'^profileModel_user/(?P<pk>[0-9]+)$',views.ProfileUserViewByID.as_view()),
]