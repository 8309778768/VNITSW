from django.contrib import admin
from myapp.models import Book
from myapp.models import Post

# Register your models here.
admin.site.register(Book)
admin.site.register(Post)
