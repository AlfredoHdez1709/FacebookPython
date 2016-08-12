from django.shortcuts import render
from django.views.generic import View

class UpdateView(View):
	def get(self,request):
		template_name = 'new.html'
		context = {}
		return render(request, template_name, context)
