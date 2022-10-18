from email import message
from msilib.schema import ListView
from re import template
#from django.shortcuts import render
from django.views import generic
#from django.views import View
from main.forms import BlogForm
from .models import (
    Blog)


class IndexView(generic.TemplateView):
	template_name = "main/index.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#userprofiles = UserProfile.objects.filter(is_active=True)
		#testimonials = Testimonial.objects.filter(is_active=True)
		#certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		#portfolio = Portfolio.objects.filter(is_active=True)
	
		#context["userprofiles"] = userprofiles
		#context["testimonials"] = testimonials
		#context["certificates"] = certificates
		context["blogs"] = blogs
		#context["portfolio"] = portfolio
		return context
class BlogAddInfo(generic.FormView):
	template_name= "main/blogaddinfo.html"
	form_class = BlogForm
	success_url = "main/blog.html"
"""
	def form_valid(self, form): 
		form.save()
		message.success(self.request,'Gracias por aportar en la página')
		return super().form_valid(form)
"""

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"