from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('game/index.html')
    context = {
        'num': 2,
    }
    return HttpResponse(template.render(context, request))

def bank(request):
	template = loader.get_template('game/bank.html')
	context = {
		'num': 2,
	}
	return HttpResponse(template.render(context, request))
