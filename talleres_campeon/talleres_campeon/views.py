from django.shortcuts import render
from api.models import New, Match, Category, Video



def home(request):
    listNewsLigaProfesional = []
    listNewsFemenino = []
    listNewsMercado = []
    for el in New.objects.all().order_by("-id")[6::]:
        match str(el.category):
            case "Liga Profesional":
                listNewsLigaProfesional.append(el)
            case "Femenino":
                listNewsFemenino.append(el)
            case "Mercado de pases":
                listNewsMercado.append(el)
    context = {
        'listNews': New.objects.all().order_by("-id"),
        'listNewsFourAndSix': New.objects.all().order_by("-id")[3:6],
        'listMatchs': Match.objects.all().order_by("-id"),
        'listCategories': Category.objects.all(),
        'listVideos': Video.objects.all().order_by("-id")[0:3],
        'listNewsLigaProfesional': listNewsLigaProfesional[0:3],
        'listNewsFemenino': listNewsFemenino[0:3],
        'listNewsMercado': listNewsMercado[0:3]
    }
    return render(request, 'home.html', context)

def newDetail(request, id):
    category = New.objects.get(id=int(id)).category
    listNewsCategory = []
    listNew = New.objects.filter(category=category).order_by("-id")
    for el in listNew:
        if int(el.id) != int(id) and len(listNewsCategory)<2:
            listNewsCategory.append(el)
    context = {
        'new': New.objects.get(id=int(id)),
        'listNewsCategory': listNewsCategory,
    }
    return render(request, 'newDetail.html', context)

def newsCategory(request, category):
    context = {
        'category': category,
        'listNews': New.objects.filter(category=Category.objects.get(name=category).id_category).order_by("-id")
    }
    return render(request, 'newsCategory.html', context)

def matches(request):
    context = {
        'listMatches': Match.objects.all().order_by("-id"),
        'matchesLiga': Match.objects.filter(tournament="Liga Profesional").order_by("-id"),
        'matchesCopaArgentina': Match.objects.filter(tournament="Copa Argentina"),
    }
    return render(request, 'partidos.html', context)