from django.db import models


class Anime(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.URLField(max_length=500, blank=True,
                            null=True)
    youtube_url = models.URLField(
        max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200)
    genres = models.JSONField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    episodes = models.IntegerField(null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    rating = models.CharField(max_length=50, blank=True, null=True)
    score = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.00)
    synopsis = models.TextField(blank=True, null=True)
    background = models.TextField(
        blank=True, null=True)
    year = models.PositiveIntegerField(
        blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
