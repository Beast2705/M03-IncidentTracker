from django.db import connection
from django.shortcuts import render, get_object_or_404
from .models import Incident

# --- VISTA 1: Buscador Vulnerable (PASO A) ---
def busqueda_vulnerable(request):
    q = request.GET.get('q', '')
    results = []
    
    if q:
        query = f"SELECT * FROM core_incident WHERE title LIKE '%{q}%'"
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    return render(request, 'busqueda.html', {'incidents': results})


# --- VISTA 2: Update Email SEGURO (Hardening / Paso 6) ---
def update_email_vulnerable(request):
    if request.method == "POST":
        new_email = request.POST.get('email')
        
        user = request.user
        user.email = new_email
        user.save() 
        
        return render(request, 'perfil.html', {'mensaje': 'Email actualizado de forma SEGURA.'})
    
    return render(request, 'perfil.html')


# --- VISTA 3: Ver Incidente SEGURO (IDOR Corregido / Paso 8) ---
def ver_incidente(request, id):
    incidente = get_object_or_404(Incident, id=id, creator=request.user) 
    
    return render(request, 'detalle.html', {'incidente': incidente})