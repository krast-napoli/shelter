from rest_framework.routers import DefaultRouter
from .views import DogsViewSet

#Here we use routers for API
router = DefaultRouter()
router.register(r'dogshelter', DogsViewSet, basename='user')

urlpatterns = router.urls

#We can also use only viewsets without routers
#from django.urls import path
#from .views import DogsView

#app_name = "dogshelter"

#urlpatterns = [
#    path('dogshelter/', DogsView.as_view({'get':'list'})),
#    path('dogshelter/<int:pk>', DogsView.as_view({'get':'retrieve'}))
#]