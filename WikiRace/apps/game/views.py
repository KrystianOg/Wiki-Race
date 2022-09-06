from rest_framework import viewsets
from .models import Game


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()

    def start(self, request):
        pass

    def step(self, request):
        pass

    def surrender(self, request):
        pass
