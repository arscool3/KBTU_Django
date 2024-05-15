from rest_framework import routers
from .views import CounterStrikeGameViewSet, CounterTerroristViewSet, TerroristViewSet, BombViewSet, MapViewSet, WeaponViewSet

router = routers.DefaultRouter()
router.register(r'counter_strike_games', CounterStrikeGameViewSet, basename='counter_strike_games')
router.register(r'counterterrorists', CounterTerroristViewSet, basename='counterterrorists')
router.register(r'terrorists', TerroristViewSet, basename='terrorists')
router.register(r'bombs', BombViewSet, basename='bombs')
router.register(r'maps', MapViewSet, basename='maps')
router.register(r'weapons', WeaponViewSet, basename='weapons')

urlpatterns = [] + router.urls
