from decimal import Decimal
from datetime import date

def calcular_nivel_riesgo(salario, nivel_riesgo):
    porcentaje_riesgo = {
        'I': Decimal('0.00522'),
        'II': Decimal('0.01044'),
        'III': Decimal('0.02436'),
        'IV': Decimal('0.04350'),
        'V': Decimal('0.06960')
    }.get(nivel_riesgo, Decimal('0'))
    return salario * porcentaje_riesgo

def calcular_dependiente(salario):
    porcentaje_salud = Decimal('0.04')
    porcentaje_pension = Decimal('0.04')
    salud = salario * porcentaje_salud
    pension = salario * porcentaje_pension
    return salud, pension

def calcular_independiente(salario):
    porcentaje_salud = Decimal('0.125')
    porcentaje_pension = Decimal('0.16')
    salud = salario * porcentaje_salud
    pension = salario * porcentaje_pension
    return salud, pension

def calcular_seguridad_social(empleado):
    if empleado.tipo_empleado == 'Dependiente':
        return calcular_dependiente(empleado.salario)
    elif empleado.tipo_empleado == 'Independiente':
        return calcular_independiente(empleado.salario)
    return Decimal('0'), Decimal('0')

def calcular_horasextras(empleado):
    # Calculamos el total de horas mensuales asumiendo 4 semanas al mes
    totalHorasMes = empleado.horas_semanales * 4
    valorhora = empleado.salario / Decimal(totalHorasMes)
    hExtraDiurna = round((valorhora * Decimal('0.25')) + valorhora, 2)
    hExtraNocturna = round((valorhora * Decimal('0.75')) + valorhora, 2)
    hExtraDDominical = round((valorhora * Decimal('2')) + valorhora, 2)
    hExtraNDominical = round((valorhora * Decimal('2.5')) + valorhora, 2)
    hRecargoDominical = round((valorhora * Decimal('0.75')) + valorhora, 2)
    hRecargoNDominical = round((valorhora * Decimal('2.1')) + valorhora, 2)
    totalHorasExtras = hExtraDiurna + hExtraNocturna + hExtraDDominical + hExtraNDominical + hRecargoDominical + hRecargoNDominical
    
    return {
        'hExtraDiurna': hExtraDiurna,
        'hExtraNocturna': hExtraNocturna,
        'hExtraDDominical': hExtraDDominical,
        'hExtraNDominical': hExtraNDominical,
        'hRecargoDominical': hRecargoDominical,
        'hRecargoNDominical': hRecargoNDominical,
        'totalHorasExtras': totalHorasExtras
    }

def calcular_prima(fecha_inicio, fecha_fin):
    mitad_ano = date(fecha_inicio.year, 6, 30)
    inicio_segunda_mitad = date(fecha_inicio.year, 7, 1)
    final_ano = date(fecha_inicio.year, 12, 31)

    if fecha_inicio <= mitad_ano and fecha_fin >= inicio_segunda_mitad:
        dias_primera_mitad = (mitad_ano - fecha_inicio).days + 1
        dias_segunda_mitad = (fecha_fin - inicio_segunda_mitad).days + 1
    elif fecha_inicio > mitad_ano:
        dias_primera_mitad = 0
        dias_segunda_mitad = (fecha_fin - fecha_inicio).days + 1
    else:
        dias_primera_mitad = (fecha_fin - fecha_inicio).days + 1
        dias_segunda_mitad = 0

    return dias_primera_mitad, dias_segunda_mitad

def calcular_cesantias(salario_total_calculado, dias_trabajados):
    return (salario_total_calculado * Decimal(dias_trabajados)) / Decimal('360')
