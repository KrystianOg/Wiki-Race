from django.db import models
import uuid


class GameType(models.Model):
    """Game type model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    rules = models.ManyToManyField('Rule', related_name='rules')
    category = models.ManyToManyField('Category', related_name='categories')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Game Type"
        verbose_name_plural = "Game Types"
        db_table = "game_types"
        ordering = ["created"]


class Rule(models.Model):
    """Rules for the game"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"
        db_table = "rules"
        ordering = ["order"]


class Category(models.Model):
    """Categories for the game"""
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"
