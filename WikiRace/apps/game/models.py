import uuid
from django.db import models


class Page(models.Model):
    """Page model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=200, unique=True)
    visits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        db_table = "pages"
        ordering = ["created"]


class GameProgress(models.Model):
    """Game progress model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.ForeignKey(Page, on_delete=models.DO_NOTHING)
    userGame = models.ForeignKey('UserGame', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page.url

    class Meta:
        verbose_name = "Game Progress"
        verbose_name_plural = "Game Progresses"
        db_table = "game_progresses"
        ordering = ["created"]


class Game(models.Model):
    """Game model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    start_page = models.ForeignKey(Page, on_delete=models.DO_NOTHING, related_name='startPage')
    end_page = models.ForeignKey(Page, on_delete=models.DO_NOTHING, related_name='endPage')
    min_steps = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('info.GameType', on_delete=models.DO_NOTHING, related_name='gameType')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        db_table = "games"
        ordering = ["-created"]


class UserGame(models.Model):
    """UserGame model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('authentication.User', on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    steps = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ended = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "UserGame"
        verbose_name_plural = "UserGames"
        db_table = "user_games"
        ordering = ["created"]
