from django.urls import path
from .views import homePageView, predictPageView, resultsPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('predict/', predictPageView, name='predict'),
    path('results/', resultsPageView, name='results'),
]
