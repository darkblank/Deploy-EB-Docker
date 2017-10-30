from django.conf.urls import url

from member.views import signup, log_in, log_out, facebook_login, profile, follow_toggle

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', log_in, name='log_in'),
    url(r'^logout$', log_out, name='log_out'),
    url(r'^facebook-login/$', facebook_login, name='facebook_login'),
    url(r'^(?P<user_pk>\d+)/profile$', profile, name='profile'),
    url(r'^(?P<user_pk>\d+)/follow_toggle$', follow_toggle, name='follow_toggle'),
]