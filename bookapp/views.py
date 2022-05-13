
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
class ListView(ListView):
    model = Book
    template_name='home.html'
    fields="__all__"
class DetailView(DetailView):
    model = Book
    template_name='post.html'    
class Create(CreateView):
    model=Book
    template_name='new.html'
    fields='__all__'  
    def form_isvalid(self,form):
        if  form.is_valid():
            form.save()
        return redirect('')   
class Update(UpdateView):
    model = Book
    template_name='edit.html'
    fields=['title','description']

class Delete(DeleteView):
    model=Book
    template_name='delete.html'
    success_url=reverse_lazy('home')
