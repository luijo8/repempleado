from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Empleado
from .form import EmpleadoForm

# Create your views here.
class InicioView(TemplateView):
    """Vista que carga página de inicio"""
    template_name='inicio.html'


class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by = 5
    ordering = 'first_name'
    context_object_name='empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista     
    
class ListByAreaEmpleado(ListView):
    template_name='persona/list_by_area.html'    
    context_object_name='empleados'
    
    def get_queryset(self):
        area=self.kwargs['shorname']
        lista = Empleado.objects.filter(       
            departamento__shor_name=area
        )
        return lista
    
class ListempleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(       
            first_name=palabra_clave
        )
        return lista   
    
class ListHabilidadesEmpleados(ListView):        
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        id_persona = self.request.GET.get("idPersona", '')
        print("id_persona: ",id_persona)
        if id_persona != None:
            if id_persona != "":
                empleado = Empleado.objects.get(id=id_persona)
                return empleado.habilidades.all()

#1.- Listar todos los empleados de la empresa ===> ListAllEmpleados
#2.- Listar todos los empleados que pertenecen a un área de la empresa ===> ListByAreaEmpleado
#3.- Listar empleados por trabajo ===> Tarea: class ListView
#4.- Listar empleados por palabrqa clave ===> ListempleadosByKword
#5.- Listar habilidades de un empleado ===> ListHabilidadesEmpleados

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #context['titulo'] = 'Empleado del Mes'
        return context


#Solo funciona con TemaplateView
class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    #fields = ('__all__')
    form_class = EmpleadoForm
    #success_url = ('/success')
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #empleado = form.save()
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('<===POST===>')
        print(request.POST)
        #print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print('<===FORM_VALID===>')
        #empleado = form.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')
    
class ListEmpleadosAdmin(ListView):
    template_name='persona/list_empleados.html'
    paginate_by = 10
    ordering = 'first_name'    
    model = Empleado
    context_object_name='empleados'    
