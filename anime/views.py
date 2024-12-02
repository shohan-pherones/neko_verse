from django.shortcuts import render, get_object_or_404
from .models import Anime
from django.core.paginator import Paginator
from .anime_recommend import get_recommendations


def anime_list(request):
    animes = Anime.objects.all()
    paginator = Paginator(animes, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'anime/anime_list.html', {'page_obj': page_obj})


def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'anime/anime_detail.html', {'anime': anime})


def anime_recommend(request):
    if request.method == "GET":
        user_input = request.GET.get('query', '')
        if user_input:
            recommended_animes = get_recommendations(user_input)
            return render(request, 'anime/anime_recommend.html', {'recommended_animes': recommended_animes or []})
    return render(request, 'anime/anime_recommend.html')
