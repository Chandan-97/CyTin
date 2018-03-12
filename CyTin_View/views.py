from django.shortcuts import render
from .models import Software
from django.http import HttpResponse
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
	}
	print(context)
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
