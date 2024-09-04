from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306173555',
        'name': 'Muhammad Jordan Ar-Razi Aziz',
        'class': 'PBP KI'
    }

    return render(request, "main.html", context)
