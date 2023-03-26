from django.urls import path,include
from .views import home,ShowAll,Create,Create_ID

urlpatterns = [
   path('',home,name="home"),
   path('all/',ShowAll,name="Showall"),
   path('create/',Create,name="Create"),
   path('create/<str:pk>/',Create_ID,name="CreateID"),
    
]
