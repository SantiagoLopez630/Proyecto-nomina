from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre', 'documento', 'email', 'genero', 'photo', 'salario', 
            'tipo_empleado', 'nivel_riesgo', 'dias_trabajados', 'horas_semanales', 
            'hExtraDiurna', 'hExtraNocturna', 'hExtraDDominical', 'hExtraNDominical', 
            'hRecargoDominical', 'hRecargoNDominical', 'fecha_inicio', 'fecha_fin'
        ]
