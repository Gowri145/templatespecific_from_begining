from django.urls import path
from app1.views import *
app_name='app1'

urlpatterns=[
    path('gowri/',gowri,name='gowri'),
    path('shivani/',shivani,name='shivani'),
    
]