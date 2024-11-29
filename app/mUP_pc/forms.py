from django import forms
from .models import PC, MantenimientoPC, DiasParaAlerta
from django.forms import Textarea, FileInput
from datetime import date

class PCForm(forms.ModelForm):    
    class Meta:
        model = PC
        fields = '__all__' 
        exclude = ['fecha_ultimo_mantenimiento']
        labels = {
            'intervalo_mantenimiento': 'intervalo mantenimiento correctivo'  # Aquí especificamos la etiqueta con tilde
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Nombre del PC'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: DEll, HP, Azuz'}),
            'número_de_inventario': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: B145C394'}),
            'encargado': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: David A. Chentes'}),
            'teléfono_encargado': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: +53589874'}),
            'descripción': Textarea(attrs={'class': 'form-control m-2', 'placeholder': 'Observaciones'}),
            'ubicación': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: oficina de ...'}),
            'costo_de_adquisición': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': '$'}),
            'fecha_de_adquisición': forms.DateInput(attrs={'class': 'form-control m-2', 'placeholder': 'Fecha'}),
            'fecha_de_retirada': forms.DateInput(attrs={'class': 'form-control m-2', 'placeholder': 'Fecha'}),
            'estado': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: bueno, malo, regular'}),
            'garantía': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: si, no'}),
            'software_instalado': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Eje: windows, linux, mac'}),
            'intervalo_mantenimiento': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Número determinado de "Días"'}),
            'imagen': FileInput(attrs={'class': 'form-control-file m-2'}),
        }


class DiasParaAlertaForm(forms.ModelForm):
    class Meta:
        model = DiasParaAlerta
        fields = '__all__'
        widgets = {
            'días': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number', 'placeholder': 'Actualmente'}),
        }


class MantenimientoPCForm(forms.ModelForm):
    class Meta:
        model = MantenimientoPC
        fields = '__all__'
        exclude = ['pc', 'tipo']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control m-2', 'placeholder': 'Fecha de inicio'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control m-2', 'placeholder': 'Hora de inicio'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control m-2', 'placeholder': 'Fecha de fin'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control m-2', 'placeholder': 'Hora de fin'}),
            'operador': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Nombre de quien lo realizó'}),
            'partes_y_piezas': Textarea(attrs={'class': 'form-control m-2', 'placeholder': 'Partes y piezas implicadas'}),
            'descripción': Textarea(attrs={'class': 'form-control m-2', 'placeholder': 'Descripción del mantenimiento'}),
            'imagen': FileInput(attrs={'class': 'form-control-file m-2'}),
        } 

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        
        if fecha_inicio:
            if fecha_inicio > date.today():
                self.add_error('fecha_inicio', 'La fecha de inicio no puede ser en el futuro.')
        else:
            self.add_error('fecha_inicio', 'La fecha de inicio es obligatoria. el formato correcto es "dd/mm/aaaa"')

        if fecha_fin:
            if fecha_fin > date.today():
                self.add_error('fecha_fin', 'La fecha de fin no puede ser en el futuro.')
        else:
            self.add_error('fecha_fin', 'La fecha de fin es obligatoria. el formato correcto es dd/mm/aaaa')

        if fecha_inicio and fecha_fin:
            if fecha_inicio > fecha_fin:
                self.add_error('fecha_inicio', 'La fecha de inicio no puede ser posterior a la fecha de fin.')
        
        return cleaned_data          
