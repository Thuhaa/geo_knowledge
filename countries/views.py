from django.shortcuts import render


def homepage_view(request):
	return render(request, 'countries/homepage.html')
# Create your views here.
