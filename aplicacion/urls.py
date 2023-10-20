from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.PrestamoView.as_view(), name='index'),
    path('eliminar/<int:prestamo_id>/', views.EliminarPrestamo.as_view(), name='eliminar_prestamo'),
    path('editar/<int:prestamo_id>/', views.EditarPrestamo.as_view(), name='editar_prestamo'),
    path('finalizar_prestamo/<int:prestamo_id>/', views.FinalizarPrestamo.as_view(), name='finalizar_prestamo'),

]