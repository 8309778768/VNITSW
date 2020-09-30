from django.shortcuts import render
from myapp.models import Book
from myapp.models import Post

# Create your views here.
def index(request):
	d=Book.objects.all()
	p=Post.objects.all()
	context={'books':d,'pdfs':p}
	return render(request,'index.html',context)
	



	


# Create your views here.
