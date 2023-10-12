from django.urls import path
from tutorials import views 
 
urlpatterns = [ 
    path('tutoriallist', views.tutorial_list),
    path('tutorialdetail/<int:pk>', views.tutorial_detail),
    path('tutoriallistpublished', views.tutorial_list_published)
]