from django.urls import path
from .views import HomeView, AboutusView, ContactusView
urlpatterns = [
    path("", HomeView.as_view(), name = "home_page"),
    path("about-us/", AboutusView.as_view(),name = "about_us_page"),
    path("contact-us/", ContactusView.as_view(),name = "contact_us_page"),
]

