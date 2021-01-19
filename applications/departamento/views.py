from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentoform
from applications.persona.models import Empleado
from .models import Departamento
from django.urls import reverse_lazy



class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoform
    success_url='/'
    
    def form_valid(self, form):
        print('<====Estamos en el FormValid===>')
        
        depto = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shortname']
        )
        depto.save()                
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depto
        )
        return super(NewDepartamentoView, self).form_valid(form)