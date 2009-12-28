#!/usr/bin/env python

from feeds import LatestEntriesForBlog

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout 

import os

style_path = os.path.join(settings.PROJECT_PATH, 'styles')

feeds = {
    'latest': LatestEntriesForBlog,
}

urlpatterns = patterns('',
    (r'^styles/(?P<path>.*)$', 'django.views.static.serve', {'document_root': style_path}),
    (r'^\w+/styles/(?P<path>.*)$', 'django.views.static.serve', {'document_root': style_path}),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    
    (r'^login/$', login, {'template_name': settings.DEFAULT_TEMPLATE + "/login.html"}),
    (r'^logout/$', logout),     

    (r'^(?P<blog_name>\w+)/login/$', login, {'template_name': settings.DEFAULT_TEMPLATE + "/login.html"}),
    (r'^(?P<blog_name>\w+)/logout/$', logout),     
    (r'^(?P<blog_name>\w+)/app/(?P<template_name>\w+)\.html', 'mtsite.mt.views.app_page'),
    (r'^(?P<blog_name>\w+)/(?P<year>\d{4})/$', 'mtsite.mt.views.archive_year'),
    (r'^(?P<blog_name>\w+)/(?P<year>\d{4})/page/(?P<page>\d+)/$', 'mtsite.mt.views.archive_year'),
    (r'^(?P<blog_name>\w+)/(?P<year>\d{4})/(?P<month>\d{2})/$', 'mtsite.mt.views.archive_month'),
    (r'^(?P<blog_name>\w+)/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page>\d+)/$', 'mtsite.mt.views.archive_month'),
    (r'^(?P<blog_name>\w+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<entry_basename>\w+)\.html', 'mtsite.mt.views.entry_detail'),
    (r'^(?P<blog_name>\w+)/index\.html$', 'mtsite.mt.views.archive_index'),
    (r'^(?P<blog_name>\w+)/page/(?P<page>\d+)/$', 'mtsite.mt.views.archive_index'),
    (r'^(?P<blog_name>\w+)/(?P<page_basename>\w+)\.html', 'mtsite.mt.views.page_detail'),
    (r'^(?P<blog_name>\w+)/(?P<category_basename>\w+)/$', 'mtsite.mt.views.archive_category'),
    (r'^(?P<blog_name>\w+)/$', 'mtsite.mt.views.archive_index'),
    
    (r'^app/(?P<template_name>\w+)\.html', 'mtsite.mt.views.app_page'),
    (r'^(?P<year>\d{4})/$', 'mtsite.mt.views.archive_year'),
    (r'^(?P<year>\d{4})/page/(?P<page>\d+)/$', 'mtsite.mt.views.archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'mtsite.mt.views.archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page>\d+)/$', 'mtsite.mt.views.archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<entry_basename>\w+)\.html', 'mtsite.mt.views.entry_detail'),
    (r'^index\.html$', 'mtsite.mt.views.archive_index'),
    (r'^page/(?P<page>\d+)/$', 'mtsite.mt.views.archive_index'),
    (r'^(?P<page_basename>\w+)\.html', 'mtsite.mt.views.page_detail'),
    (r'^(?P<category_basename>\w+)/$', 'mtsite.mt.views.archive_category'),
    (r'^$', 'mtsite.mt.views.archive_index'),
 )
