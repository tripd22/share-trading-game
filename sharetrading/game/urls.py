from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('savingsaccount', views.savingsaccount, name='savingsaccount'),
        path('housing', views.housing, name='housing'),
        path('shares', views.shares, name='shares'),
        path('riskandreturn', views.riskandreturn, name='riskandreturn'),
        path('activeandpassive', views.activeandpassive, name='activeandpassive'),
        path('timingthemarket', views.timingthemarket, name='timingthemarket'),
        path('transactioncosts', views.transactioncosts, name='transactioncosts'),
        path('diversification', views.diversification, name='diversification'),
        path('otherinvestments', views.otherinvestments, name='otherinvestments'),
        path('learnmore', views.learnmore, name='learnmore')
]
