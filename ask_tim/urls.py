from django.conf.urls import patterns, include, url

from django.contrib import admin
from ask_app import views as ask_views

admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ask_views.index, name='index'),
    url(r'^login', ask_views.login, name='login'),
    url(r'^signup', ask_views.signup, name='signup'),
    url(r'^ask', ask_views.ask, name='ask'),
    url(r'^question/(?P<question_id>\d+)/$', ask_views.question, name='question'),
    url(r'^tag/(?P<tagName>[\w\-]+)/$', ask_views.tag, name='tag'),
    url(r'^hot', ask_views.hot, name='hot'),
)
