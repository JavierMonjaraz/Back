from django.urls import path, re_path

from sign_up import views

urlpatterns=[
    re_path(r'^signup', views.SignUpModelView.as_view())
]