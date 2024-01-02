from django.shortcuts import render, redirect
from .models import Empleado,Cargo,Calculo
from decimal import Decimal

# Create your views here.
def home(request):
	return render(request, "inicio.html", {})

def empleadosVista(request):
    datos = Empleado.objects.select_related('cargo').values(
        'id', 'nombre', 'apellido', 'codigo', 'salario', 'cargo__nombre_cargo'
    )
    cargos = Cargo.objects.all()
    return render(request, "empleados.html", {"emp": datos, "cargos":cargos})

def registrarEmpleado(request):
	if request.method == 'POST':
		cargo_id = request.POST['cargo']
		cargo = Cargo.objects.get(pk=cargo_id)
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		codigo = request.POST['codigo']
		salario = request.POST['salario']

		em = Empleado.objects.create(nombre=nombre,apellido=apellido,codigo=codigo,salario=salario,cargo=cargo)
		return redirect('/empleados')

def editarEmpleado(request, id):
    cargos = Cargo.objects.all()
    empleado = Empleado.objects.select_related('cargo').filter(id=id).values(
        'id', 'nombre', 'apellido', 'codigo', 'salario', 'cargo__nombre_cargo', 'cargo__id'
    ).first()
    
    return render(request, 'editarEmpleado.html', {'empleado': empleado, "cargos": cargos})

def editandoEmpleado(request):
	cargo_id = request.POST['cargo']
	cargo = Cargo.objects.get(pk=cargo_id)
	emId = int(request.POST['id'])
	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	edad = request.POST['edad']
	codigo = request.POST['codigo']
	salario = request.POST['salario']

	empleado = Empleado.objects.get(id=emId)
	empleado.nombre = nombre
	empleado.apellido = apellido
	empleado.codigo = codigo
	empleado.edad = edad
	empleado.salario = salario
	empleado.cargo = cargo
	empleado.save()
	return redirect('/empleados')

def eliminarEmpleado(request, id):
	empleado = Empleado.objects.get(id=id)
	empleado.delete()
	return redirect('/empleados')

def irPagar(request):
    empleados = Empleado.objects.all()
    if request.method == 'POST' and 'empleado' in request.POST:
        empleado_id = request.POST['empleado']
        empleadoEncontrado = Empleado.objects.select_related('cargo').filter(pk=empleado_id).values(
            'id', 'nombre', 'apellido', 'codigo', 'salario', 'cargo__nombre_cargo', 'cargo__id'
        ).first()
        return render(request, "pago.html", {"empleados": empleados, "empleadoEncontrado": empleadoEncontrado})
    else:
        return render(request, "pago.html", {"empleados": empleados})

from django.shortcuts import redirect

def calcular(request):
    if request.method == 'POST' and 'empleado_id' in request.POST:
        idEmpleado = request.POST['empleado_id']
        empleado = Empleado.objects.get(pk=idEmpleado)
        descuentoRenta = Decimal('0.00')
        descuentoAFP = float(empleado.salario) * 0.0725
        descuentoISSS = float(empleado.salario) * 0.03
        if float(empleado.salario) > 498.00:
            descuentoRenta = float(empleado.salario) * 0.10
        else:
            descuentoRenta = Decimal('0.00')

        totalDescuento = descuentoRenta + descuentoAFP + descuentoISSS
        pagoFinal = float(empleado.salario) - totalDescuento

        calculo = Calculo.objects.create(desAFP=Decimal(str(descuentoAFP)), desRENTA=Decimal(str(descuentoRenta)), 
                                         desISSS=Decimal(str(descuentoISSS)), empleado_id=idEmpleado)

        resultados = Calculo.objects.filter(empleado_id=idEmpleado)

        return render(request, "pago.html", {"descuentosCalculados":resultados, "descuento":totalDescuento, "final":pagoFinal})
    else:
        return redirect('pago')
