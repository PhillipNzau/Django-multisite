from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "products.html", {})