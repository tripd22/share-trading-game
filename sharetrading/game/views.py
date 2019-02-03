from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('game/index.html')
    context = {
        'num': 2,
    }
    return HttpResponse(template.render(context, request))

def savingsaccount(request):
	template = loader.get_template('game/savingsaccount.html')
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

def activeandpassive(request):
	template = loader.get_template('game/activeandpassive.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def timingthemarket(request):
	template = loader.get_template('game/timingthemarket.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def transactioncosts(request):
	template = loader.get_template('game/transactioncosts.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def diversification(request):
	template = loader.get_template('game/diversification.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def otherinvestments(request):
	template = loader.get_template('game/otherinvestments.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))

def learnmore(request):
	template = loader.get_template('game/learnmore.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))