from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('bankaccount', views.bankaccount, name='bankaccount'),
        path('housing', views.housing, name='housing'),
        path('shares', views.shares, name='shares'),
        path('riskandreturn', views.riskandreturn, name='riskandreturn')
]
