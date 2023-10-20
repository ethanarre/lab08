from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.db.models import Q
from django.utils import timezone


class PrestamoView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        listaPrestamos = Prestamos.objects.all()

        if query:
            listaPrestamos = listaPrestamos.filter(Q(libro_id__titulo__icontains=query))

        formPrestamo = PrestamoForm()  # Crear una instancia del formulario

        context = {
            'Prestamos': listaPrestamos,
            'query': query,
            'formPrestamo': formPrestamo,  # Pasar el formulario al contexto
        }
        return render(request, 'index.html', context)
        
    def post(self, request):
        formPrestamos = PrestamoForm(request.POST)
        if formPrestamos.is_valid():
            formPrestamos.save()
            return redirect('web:index')
        
        
class EliminarPrestamo(View):
    def post(self,request,prestamo_id):
        prestamo = Prestamos.objects.get(pk=prestamo_id)
        prestamo.delete()
        return redirect('web:index')
    
class EditarPrestamo(View):
    def get(self, request, prestamo_id):
        prestamo = Prestamos.objects.get(pk=prestamo_id)
        form = PrestamoForm(instance=prestamo)
        context = {
            'formPrestamo': form,
            'prestamo_id': prestamo_id
        }
        return render(request, 'editar_prestamo.html', context)
    
    def post(self, request, prestamo_id):
        prestamo = Prestamos.objects.get(pk=prestamo_id)
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('web:index')
    
class FinalizarPrestamo(View):
    def post(self, request, prestamo_id):
        prestamo = Prestamos.objects.get(pk=prestamo_id)
        prestamo.FecDevolucion = timezone.now()
        prestamo.finalizado = True
        prestamo.save()
        return redirect('web:index')



    

