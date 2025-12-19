from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("standards/", views.standards, name="standards"),
    path("signup/", views.signup, name="signup"),
    path("documents/", views.documents),
    path("news/", views.news),
    path("partners/", views.partners),

]
