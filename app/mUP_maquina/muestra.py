@login_required
def mod_mantenimiento_maquina_correctivo(request, id):
    if request.method == 'GET':
        mantenimiento = get_object_or_404(MantenimientoMaquina, id=id)
        maquina = mantenimiento.maquina
        form_mant = MantenimientoMaquinaCorrectivoForm(instance=mantenimiento)
        context = {
            'form_mant': form_mant,
            'maquina': maquina,
        }
        return render(request, 'mUP_maquina/mod_mantenimineto_correctivo.html', context)
    
    if request.method == 'POST':
        mantenimiento = get_object_or_404(MantenimientoMaquina, id=id)
        tipo_mantenimiento = get_object_or_404(TipoMantenimientoMaquina, id=1) 
        maquina = mantenimiento.maquina
        form_mant = MantenimientoMaquinaCorrectivoForm(request.POST, request.FILES, instance=mantenimiento)

        if form_mant.is_valid():
            mantenimiento = form_mant.save(commit=False)
            mantenimiento.maquina = maquina
            mantenimiento.tipo = tipo_mantenimiento

            if form_mant.cleaned_data['hr_maquina'] > maquina.horas_máquina_trabajada:
                form_mant.add_error('hr_maquina', 'Las horas de trabajo del mantenimiento no pueden ser mayores que las horas de trabajo de la máquina.')
                context = {
                    'form_mant': form_mant,
                    'maquina': maquina,
                    'tipo_mantenimiento': tipo_mantenimiento,
                }
                messages.error(request, "Alguno de los datos introducidos no son válidos, revise nuevamente cada campo") 
                return render(request, 'mUP_maquina/nuevo_mantenimineto_correctivo.html', context)
            else:
                if 'imagen' in request.FILES:
                    mantenimiento.imagen = request.FILES['imagen'] 
                mantenimiento.save()
                return redirect('mantenimientos_maquina_correctivo', id=maquina.id)
        else:
            context = {
                'form_mant': form_mant,
                'maquina': maquina,
            }
            messages.error(request, "Alguno de los datos introducidos no son válidos, revise nuevamente cada campo") 
            return render(request, 'mUP_maquina/mod_mantenimineto_correctivo.html', context)

    return HttpResponse("Method Not Allowed", status=405)