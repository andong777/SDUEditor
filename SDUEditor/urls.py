from django.conf.urls import patterns, include, url

from django.contrib import admin
from SDUEditor import settings
from App import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SDUEditor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'file/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.FILE_PATH}),
    url(r'css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_PATH}),
    url(r'js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_PATH}),
    url(r'img/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.IMG_PATH}),
    url(r'^$',views.home),
    url(r'editor/$',views.editor),
    url(r'edit_new$',views.edit_new),
    url(r'^save/$',views.save),
    url(r'^load/$',views.load),
    url(r'^search/$',views.search),
)
