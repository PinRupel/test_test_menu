from django.shortcuts import render

def menu(request):
    return render(request, "menu/menu.html")

def pos_menu(request, slug):
    context = {
        'slug': slug,
    }
    return render(request, "menu/pos_menus.html", context)