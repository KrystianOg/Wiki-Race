from django.urls import path

from . import views


urlpatterns = [
    path('start', views.GameViewSet.as_view({'post': 'start'}), name='start'),
    path('step', views.GameViewSet.as_view({'post': 'step'}), name='step'),
    path('surrender', views.GameViewSet.as_view({'post': 'surrender'}), name='surrender'),
]
