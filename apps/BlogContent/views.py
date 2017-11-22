from django.shortcuts import render
from django.views.generic import CreateView, ListView
from apps.BlogContent.models import BlogPost
from apps.BlogContent.forms import BlogForm

# Create your views here.

class SeeBP(ListView):
	model = BlogPost
	template_name ='blog/blog.html'
	paginate_by = 3
	ordering = ['-upload_date']
	
