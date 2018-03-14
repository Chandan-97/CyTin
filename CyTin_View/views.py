from django.shortcuts import render
from django.http import HttpResponse

from .models import Software
from .models import News

from .tags import getTags

# Create your views here.

def home(request):
	query = Software.objects.all();
	context = {
		"item_list" : query,
		"active" : "home",
	}
	return render(request, "home.html", context)

def test(request, id):
	res = "<h1>Hello World </h1>"
	return HttpResponse(res)

def details(request, id):
	query = Software.objects.filter(pk=id)
	# print(query)
	context = {
		"items" : query,
		"active" : "home",
	}
	return render(request, "details.html", context)

def categories(request):
	query = Software.objects.all()
	res_str = ""
	for q in query:
		res_str += (" " + q.category)
	tags = getTags(res_str)

	context = {
		"tags" : tags,
		"active" : "categories",
	}
	
	print(context)
	return render(request, "categories.html", context)
	# return test(request, 1)

def newlyadded(request):
	query = Software.objects.all().order_by("-timestamp")
	context = {
		"item_list" : query,
		"active" : "newlyadded",
	}
	print(context)
	return render(request, "home.html", context)
	# return test(request, 1)

def majoros(request):
	query = Software.objects.filter(isos=True)
	context = {
		"item_list" : query,
		"active" : "majoros",
	}
	print(context)
	return render(request, "home.html", context)
	# return test(request, 1)

def news(request):
	query = News.objects.all().order_by("-timestamp")

	context = {
		"news_list" : query,
		"active" 	: "news",
	}

	return render(request, "news.html", context)

def news_details(request, id):
	query = News.objects.filter(pk=id)
	context = {
		"news" : query,
		"active" : "news",
	}

	return render(request, "news_details.html", context)

def requested(request):
	query = Software.objects.filter(isRequested=True).order_by("-timestamp")
	context = {
		"item_list" : query,
		"active" 	: "requested",
	}

	return render(request, "home.html", context)