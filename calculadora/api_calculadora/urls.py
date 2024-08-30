from django.urls import path
from.views import SumaView,RestaView,MultiplicationView,DivisionView


urlpatterns = [
    path('sumar/', SumaView.as_view(), name='sumar'),
    path('restar/', RestaView.as_view(), name='restar'),
    path('multiplicar/', MultiplicationView.as_view(), name='restar'),
    path('division /', DivisionView.as_view(), name='dividir'),

]
