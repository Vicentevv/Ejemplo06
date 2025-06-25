from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# Importar las clases de models.py
from administrativo.models import Matricula, Estudiante, Modulo
from administrativo.forms import MatriculaForm, MatriculaEditForm

# Vista que permita presentar las matriculas
# El nombre de la vista es index.

def index(request):
    """
    Vista para listar las matrículas de los estudiantes.
    """
    matriculas = Matricula.objects.all()
    estudiantes = Estudiante.objects.all()  # Obtener todos los estudiantes

    titulo = "Listado de matriculas"

    # Pasar las matrículas, estudiantes y su costo total calculado
    informacion_template = {
        'matriculas': matriculas,
        'numero_matriculas': len(matriculas),
        'mititulo': titulo,
        'estudiantes': estudiantes  # Estudiantes ya tienen el método calcular_costo_total
    }

    return render(request, 'index.html', informacion_template)


def detalle_matricula(request, id):
    """
    """

    matricula = Matricula.objects.get(pk=id)
    informacion_template = {'matricula': matricula}
    return render(request, 'detalle_matricula.html', informacion_template)


def crear_matricula(request):
    """
    """
    estudiantes = Estudiante.objects.all()  # Obtener todos los estudiantes
    modulos = Modulo.objects.all()  # Obtener todos los módulos

    if request.method == 'POST':
        formulario = MatriculaForm(request.POST)
        if formulario.is_valid():
            formulario.save()  # Se guarda en la base de datos
            return redirect(index)
    else:
        formulario = MatriculaForm()

    diccionario = {
        'formulario': formulario,
        'estudiantes': estudiantes,
        'modulos': modulos
    }

    return render(request, 'crear_matricula.html', diccionario)


def editar_matricula(request, id):
    """
    """
    matricula = Matricula.objects.get(pk=id)
    if request.method == 'POST':
        formulario = MatriculaEditForm(request.POST, instance=matricula)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MatriculaEditForm(instance=matricula)
    diccionario = {'formulario': formulario}

    return render(request, 'crear_matricula.html', diccionario)


def detalle_estudiante(request, id):
    """
    """

    estudiante = Estudiante.objects.get(pk=id)
    informacion_template = {'e': estudiante}
    return render(request, 'detalle_estudiante.html', informacion_template)
