import requests
from django.core.management.base import BaseCommand
from anime.models import Anime


class Command(BaseCommand):
    help = 'Fetch anime data from Jikan API and populate the Anime model'

    def handle(self, *args, **kwargs):
        url = "https://api.jikan.moe/v4/anime"
        params = {
            'page': 1,
        }

        response = requests.get(url, params=params)
        data = response.json()

        for anime_data in data['data']:
            anime, created = Anime.objects.update_or_create(
                id=anime_data['mal_id'],
                defaults={
                    'image': anime_data['images']['jpg']['image_url'],
                    'youtube_url': anime_data.get('trailer', {}).get('url', ''),
                    'title': anime_data['title'],
                    'type': anime_data.get('type', ''),
                    'episodes': anime_data['episodes'] if 'episodes' in anime_data else 0,
                    'status': anime_data.get('status', ''),
                    'rating': anime_data.get('rating', ''),
                    'score': anime_data.get('score', 0.00),
                    'synopsis': anime_data.get('synopsis', ''),
                    'background': anime_data.get('background', ''),
                    'year': anime_data.get('aired', {}).get('from', '').split('-')[0] if anime_data.get('aired') else None
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Anime '{anime.title}' added successfully."))
            else:
                self.stdout.write(self.style.SUCCESS(
                    f"Anime '{anime.title}' updated successfully."))
