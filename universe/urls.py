# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
          url(r'^$', views.overview, name='overview'),         
          url(r'^economy/$', views.economyView.as_view(), name='economy'),
          #url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
          url(r'^military/$', views.militaryView.as_view(), name='military'),
          #url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
          url(r'^player/$', views.humansView.as_view(), name='player'),
          #url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
          #url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
          ]