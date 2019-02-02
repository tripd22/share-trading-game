from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('game/index.html')
    context = {
        'num': 2,
    }
    return HttpResponse(template.render(context, request))

def bankaccount(request):
	template = loader.get_template('game/bankaccount.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def housing(request):
	template = loader.get_template('game/housing.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def shares(request):
	template = loader.get_template('game/shares.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def riskandreturn(request):
	template = loader.get_template('game/riskandreturn.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))