from django.urls import path

from . import views

app_name = 'comparison'

urlpatterns =[
  path('',views.Index, name='index'),
  path('result/<int:trip_output_id>', views.Result, name='result'),
  path('compare/<int:trip_input_id>',views.Compare,name='compare')
]