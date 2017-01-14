from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.questionnaire, name='questionnaire'),
    url(r'^answers', views.answers, name='answers'),
]
