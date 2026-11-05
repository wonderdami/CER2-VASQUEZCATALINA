from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Mascota, Especie

def home_view(request):
    return render(request, 'app/home.html')

def catalogo_view(request):
    especie_id = request.GET.get('especie')
    
    if especie_id:
        mascotas = Mascota.objects.filter(especie_id=especie_id)
    else:
        mascotas = Mascota.objects.all()
        
    especies = Especie.objects.all()

    return render(request, 'app/catalogo.html', {
        'mascotas': mascotas,
        'especies': especies,
        'especie_seleccionada': especie_id
    })
def detalle_mascota_view(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'app/detalle.html', {'mascota': mascota})

@login_required(login_url='login')
@permission_required('app.add_mascota', raise_exception=True)
def gestion_mascotas_view(request):
    mascotas = Mascota.objects.all()
    return render(request, 'app/gestion.html', {'mascotas': mascotas})