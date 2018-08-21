from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# Create your views here.
#Uso reverse_lazy poiche se usassi, nella view class-based, reverse() mi importerebbe Sito_WasteManager.urls e comporterebbe quindi una dipendeza circolare
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
