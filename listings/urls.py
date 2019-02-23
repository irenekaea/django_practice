from django.urls import path
from . import views # Import all views from this folder

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]