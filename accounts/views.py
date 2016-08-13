from django.shortcuts import render, redirect
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm






class Alta(View):
	def get(self,request):
		template_name = 'accounts/alta.html'
		form = RegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			#aqui le voy a asignar un perfil al usuario
			#perfil_nuevo = Perfil()
			#perfil_nuevo.user = new_user
			#perfil_nuevo.save()
			return redirect('login')
		else:
			context = {
			'form':form,
			}
			template_name = 'accounts/alta.html'
			return render(request,template_name,context)



