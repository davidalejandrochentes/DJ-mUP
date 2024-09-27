from django import forms
from .models import Vehiculo, MantenimientoVehiculo, KmParaAlerta 
from django.forms import Textarea, FileInput
from datetime import date

class VehiculoForm(forms.ModelForm):    
    class Meta:
        model = Vehiculo
        fields = '__all__' 
        exclude = ['fecha_ultimo_mantenimiento']
        labels = {
            'intervalo_mantenimiento': 'Intervalo entre manteniminetos correctivos',
            'intervalo_cambio_filtro_aceite': 'Intervalo entre manteniminetos para cambio del filtro de aceite',
            'intervalo_cambio_filtro_aire_combustible': 'Intervalo entre manteniminetos para cambio del filtro de aire y combustible',
            'intervalo_cambio_aceite_caja_corona': 'Intervalo entre manteniminetos para cambio del filtro de caja y corona',
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: KIA'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: Picanto'}),
            'matrícula': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: B1542C'}),
            'número_de_chasis': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: 458979BD56'}),
            'capacidad_de_carga': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: 3 personas, 1 tonelada'}),
            'uso_del_vehiculo': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: trasporte de carga, pasajeros ...'}),
            'km_recorridos': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'km?'}),
            
            'intervalo_mantenimiento': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Número determinado en Km'}),
            'intervalo_cambio_filtro_aceite': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Número determinado en Km'}),
            'intervalo_cambio_filtro_aire_combustible': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Número determinado en Km'}),
            'intervalo_cambio_aceite_caja_corona': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Número determinado en Km'}),
            
            'imagen': FileInput(attrs={'class': 'form-control-file m-2'}),

            'nombre_chofer': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: Juan Chentes'}),
            'teléfono_chofer': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: +53589874'}),
            'dirección_chofer': Textarea(attrs={'class': 'form-control m-2', 'placeholder': 'Dirección'}),
            'dni_chofer': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'DNI?'}),
        }


class MantenimientoVehiculoForm(forms.ModelForm):
    class Meta:
        model = MantenimientoVehiculo
        fields = '__all__'
        exclude = ['vehiculo', 'tipo']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control m-2', 'placeholder': 'Fecha de inicio'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control m-2', 'placeholder': 'Hora de inicio'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control m-2', 'placeholder': 'Fecha de fin'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control m-2', 'placeholder': 'Hora de fin'}),
            'km_recorridos': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Km?'}),
            'operador': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Nombre de quien lo realizó'}),
            'descripción': forms.Textarea(attrs={'class': 'form-control m-2', 'placeholder': 'Descripción del mantenimiento'}),
            'partes_y_piezas': forms.Textarea(attrs={'class': 'form-control m-2', 'placeholder': 'Partes y piezas implicadas'}),
            'imagen': FileInput(attrs={'class': 'form-control-file m-2'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        km_recorridos = cleaned_data.get('km_recorridos')
        
        if fecha_inicio > date.today():
            self.add_error('fecha_inicio', 'La fecha de inicio no puede ser en el futuro.')
        
        if fecha_fin > date.today():
            self.add_error('fecha_fin', 'La fecha de fin no puede ser en el futuro.')

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            self.add_error('fecha_inicio', 'La fecha de inicio no puede ser posterior a la fecha de fin.')
        
        if km_recorridos < 1:
            self.add_error('km_recorridos', 'El valor de "km recorridos" no puede ser un número negativo')
        
        return cleaned_data



class KmParaAlertaForm(forms.ModelForm):
    class Meta:
        model = KmParaAlerta
        fields = '__all__'
        widgets = {
            'km': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Actualmente'}),
        }   