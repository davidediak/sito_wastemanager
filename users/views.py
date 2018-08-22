from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
#Uso reverse_lazy poiche se usassi, nella view class-based, reverse() mi importerebbe Sito_WasteManager.urls e comporterebbe quindi una dipendeza circolare
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile(request, u_id):
    user =  get_object_or_404(CustomUser, pk=u_id)
    context = {'user': user}
    return render(request, "users/detail.html", context)



