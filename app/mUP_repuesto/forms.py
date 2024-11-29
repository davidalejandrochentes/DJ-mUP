from django import forms
from .models import Maquina, Parte, Inventario

class MaquinaRepuestoForm(forms.ModelForm):    
    class Meta:
        model = Maquina
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Nombre de la máquina'}),            
        }

class ParteRepuestoForm(forms.ModelForm):    
    class Meta:
        model = Parte
        fields = '__all__'
        exclude = ['maquina']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Nombre de la parte'}),            
        }

class InventarioRepuestoForm(forms.ModelForm):    
    class Meta:
        model = Inventario
        fields = '__all__'
        exclude = ['parte']
        labels = {
            'und': 'UND',
            #'partes': 'Parte de la máquina'
        }
        widgets = {
            #'parte': forms.Select(attrs={'class': 'form-select m-2'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control m-2'}),
            'rosca': forms.TextInput(attrs={'class': 'form-control m-2'}),
            'largo': forms.TextInput(attrs={'class': 'form-control m-2'}),
            'und': forms.TextInput(attrs={'class': 'form-control m-2'}),
            'cantidad_necesaria': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number'}),         
            'existencia_stock': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number'}),         
            'salida': forms.NumberInput(attrs={'class': 'form-control m-2', 'type': 'number'}),         
        }