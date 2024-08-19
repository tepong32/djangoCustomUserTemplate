from django.shortcuts import render
from .models import User
# Create your views here.

def home(request):
	context = {
		"users": User.objects.all()
	}
	return render(request, 'users/_userBase.html', context)
