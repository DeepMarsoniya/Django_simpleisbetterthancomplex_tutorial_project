from django.http import HttpResponse


# here in home ide shows warning like request param is unused,
# but id you will remove it, it will stop working
# I don't know why but I think it will not match the handler function identity	
def home(request):
	return HttpResponse('Hello, World!')
