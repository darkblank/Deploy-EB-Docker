from django.conf.urls import url

from post.views import post_list, post_add, comment_add, post_detail, post_delete, comment_delete, post_like_toggle

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^add/$', post_add, name='post_add'),
    url(r'^(?P<pk>\d+)/comment/add/$', comment_add, name='comment_add'),
    url(r'^(?P<post_pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/delete$', post_delete, name='post_delete'),
    url(r'^(?P<comment_pk>\d+)/comment/delete$', comment_delete, name='comment_delete'),
    url(r'^(?P<post_pk>\d+)/like-toggle/$', post_like_toggle, name='post_like_toggle' ),
]
