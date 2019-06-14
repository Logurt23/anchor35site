from django.urls import path
from django.views.generic import TemplateView
from .views  import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'))

]
