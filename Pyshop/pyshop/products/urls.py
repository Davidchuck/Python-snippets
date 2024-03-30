from django.urls import path
from . import views #imports view from currect directory


urlpatterns=[
    path('',views.index),#represents root of the app
    path('test',views.new) # test is the name to add in the url path eg products/test, views.new links to the content to display.
    
    

]