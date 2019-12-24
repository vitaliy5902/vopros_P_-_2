from django.contrib import admin
from django.urls import path
from firstapp import views
urlpatterns =[path('', views.index, name='home'),
path('aa', views.fapp_aa, name='fapp_aa'),
path('clr/<str:productid>/', views.colr),
]
