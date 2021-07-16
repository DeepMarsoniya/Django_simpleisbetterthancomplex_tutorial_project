from django.http import HttpResponse
from django.shortcuts import render
from .models import Board


# here in home ide shows warning like request param is unused,
# but id you will remove it, it will stop working
# I don't know why but I think it will not match the handler function identity
def home(request):
	boards = Board.objects.all()


	return render(request,'home.html',{'boards':boards})