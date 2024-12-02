from django.shortcuts import render, get_object_or_404
from .models import Anime
from django.core.paginator import Paginator


def anime_list(request):
    animes = Anime.objects.all()
    paginator = Paginator(animes, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'anime/anime_list.html', {'page_obj': page_obj})


def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'anime/anime_detail.html', {'anime': anime})
