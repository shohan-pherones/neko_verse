import requests
from django.core.management.base import BaseCommand
from anime.models import Anime


class Command(BaseCommand):
    help = 'Fetches anime data from Jikan API and populates the database'

    def handle(self, *args, **kwargs):
        base_url = 'https://api.jikan.moe/v4/anime'
        page = 1
        while True:
            response = requests.get(f'{base_url}?page={page}')
            data = response.json()

            if page == 20 or 'data' not in data or not data['data']:
                break

            for anime in data['data']:
                Anime.objects.get_or_create(
                    id=anime['mal_id'],
                    defaults={
                        'image': anime['images']['jpg']['large_image_url'],
                        'youtube_url': anime.get('trailer', {}).get('url', ''),
                        'title': anime['title'],
                        'genres': [genre['name']
                                   for genre in anime.get('genres', [])],
                        'type': anime.get('type', ''),
                        'episodes': anime['episodes'] if 'episodes' in anime else 0,
                        'status': anime.get('status', ''),
                        'rating': anime.get('rating', ''),
                        'score': anime.get('score', 0.00),
                        'synopsis': anime.get('synopsis', ''),
                        'background': anime.get('background', ''),
                        'year': anime.get('aired', {}).get('from', '').split('-')[0] if anime.get('aired') else None
                    }
                )

            page += 1
            self.stdout.write(self.style.SUCCESS(f'Fetched page {page - 1}'))

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with anime data'))
