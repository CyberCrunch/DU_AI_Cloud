# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
          url(r'^$', views.jobboard, name='jobboard'),         
          url(r'^employees/$', views.EmployeeListView.as_view(), name='employees'),
          url(r'^employee/(?P<pk>\d+)$', views.EmployeeDetailView.as_view(), name='employee-detail'),

          #url(r'^createjob/$', views.CreateJobView, name='joblist'),
          url(r'^list/$', views.OperationListView.as_view(), name='op-list'),
          url(r'^operation/(?P<pk>\d+)$', views.OperationDetailView.as_view(), name='op-detail'),
          url(r'^myjobs/$', views.FilledJobsListView.as_view(), name='my-jobs'),
          url(r'^job/(?P<pk>[-\w]+)/create/$', views.Create_Project_Legate, name='create-job-legate'),
          
          #url(r'^employee/create/$', views.AuthorCreate.as_view(), name='author_create'),
          
          #url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
          #url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
          ]