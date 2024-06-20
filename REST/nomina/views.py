from datetime import date
from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Empleado
from rest_framework import viewsets
from nomina.forms import EmpleadoForm
from .serializer import EmpleadoSerializer
from .services import calcular_seguridad_social, calcular_nivel_riesgo, calcular_horasextras, calcular_prima, calcular_cesantias

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset=Empleado.objects.all()
    serializer_class=EmpleadoSerializer
    
@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the Employee API"})

@api_view(['GET'])
def empleadolist(request):
    get_empleados = Empleado.objects.all()
    serializer = EmpleadoSerializer(get_empleados, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearEmpleado(request):
    serializer = EmpleadoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def seguridad_social1(request, id_empleado):
    empleado = get_object_or_404(Empleado, pk=id_empleado)
    salud, pension = calcular_seguridad_social(empleado)
    nivel_riesgo_valor = calcular_nivel_riesgo(empleado.salario, empleado.nivel_riesgo)
    total_seguridad_social = salud + pension + nivel_riesgo_valor
    
    return Response({
        'empleado': EmpleadoSerializer(empleado).data,
        'salud': salud,
        'pension': pension,
        'nivel_riesgo_valor': nivel_riesgo_valor,
        'total_seguridad_social': total_seguridad_social,
    })

@api_view(['GET'])
def detalle_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, pk=id_empleado)
    salud, pension = calcular_seguridad_social(empleado)
    nivel_riesgo_valor = calcular_nivel_riesgo(empleado.salario, empleado.nivel_riesgo)
    total_seguridad_social = salud + pension + nivel_riesgo_valor
    
    if empleado.fecha_inicio and empleado.fecha_fin:
        dias_primera_mitad, dias_segunda_mitad = calcular_prima(empleado.fecha_inicio, empleado.fecha_fin)
    else:
        dias_primera_mitad = 0
        dias_segunda_mitad = 0

    horas_extras = calcular_horasextras(empleado)

    salario_total_calculado = empleado.salario + Decimal('162000')
    cesantias_calculadas = (salario_total_calculado * Decimal(empleado.dias_trabajados)) / Decimal('360')
    intereses_cesantias = (cesantias_calculadas * Decimal('0.12')) / Decimal('360')

    return Response({
        'empleado': EmpleadoSerializer(empleado).data,
        'salud': salud,
        'pension': pension,
        'nivel_riesgo_valor': nivel_riesgo_valor,
        'total_seguridad_social': total_seguridad_social,
        'dias_primera_mitad': dias_primera_mitad,
        'dias_segunda_mitad': dias_segunda_mitad,
        'dias_trabajados': empleado.dias_trabajados,
        'nivel_riesgo': empleado.nivel_riesgo,
        'cesantias': cesantias_calculadas.quantize(Decimal('1.00')),
        'intereses_cesantias': intereses_cesantias.quantize(Decimal('1.00')),
        **horas_extras
    })

@api_view(['POST'])
def cesantias_calculator(request):
    salario_mensual = Decimal(request.data.get('salario', 0))
    dias_trabajados = int(request.data.get('dias_trabajados', 0))
    
    auxilio_transporte = Decimal('162000')
    
    if salario_mensual < Decimal('1300000'):
        return Response({'error': 'El salario mensual no puede ser menor que 1300000.'}, status=status.HTTP_400_BAD_REQUEST)

    salario_total_calculado = salario_mensual + auxilio_transporte
    cesantias_calculadas = calcular_cesantias(salario_total_calculado, dias_trabajados)
    intereses_calculados = cesantias_calculadas * Decimal('0.12') / Decimal('360')

    return Response({
        'salario_mensual': salario_mensual,
        'dias_trabajados': dias_trabajados,
        'auxilio_transporte': auxilio_transporte,
        'cesantias': cesantias_calculadas.quantize(Decimal('1.00')),
        'intereses_cesantias': intereses_calculados.quantize(Decimal('1.00')),
        'salario_total': salario_total_calculado,
    })

@api_view(['GET'])
def detalle_cesantias(request, id_empleado):
    empleado = get_object_or_404(Empleado, pk=id_empleado)

    if not (empleado.salario and empleado.dias_trabajados):
        return Response({'error': 'El empleado no tiene suficiente información para calcular las cesantías.'}, status=status.HTTP_400_BAD_REQUEST)

    salario_total_calculado = empleado.salario + Decimal('162000') 
    cesantias_calculadas = calcular_cesantias(salario_total_calculado, empleado.dias_trabajados)

    return Response({
        'empleado': EmpleadoSerializer(empleado).data,
        'cesantias': cesantias_calculadas.quantize(Decimal('1.00')),
    })
