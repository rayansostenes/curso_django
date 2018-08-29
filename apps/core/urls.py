from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from core.views import PersonCreate, PersonList, PersonDelete, PersonUpdate


urlpatterns = [
    url('person/create$', PersonCreate.as_view()),
    url('person/list$', PersonList.as_view()),
    path('person/<pk>/delete', PersonDelete.as_view()),
    path('person/<pk>/update', PersonUpdate.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
]