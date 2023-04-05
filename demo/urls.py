from django.urls import path
from .views import homePageView, predictPageView, predictPost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('predict/', predictPageView, name='predict'),
    path('results/<int:time>/<int:age>/<str:serum_creatinine>/<int:serum_sodium>/<int:ejection_fraction>/',
         results, name='results'),
    path('predictPost/', predictPost, name='predictPost'),
]
