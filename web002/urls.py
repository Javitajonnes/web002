from django.contrib import admin
from django.urls import path
from ot import views as views_ot
from core import views as views_core

urlpatterns = [
    path('',views_core.home, name="home"),
    path('category/<int:id_category>/',views_ot.category,name="category"),
    path('list/',views_ot.myorder,
         name="list"),
    path('admin/', admin.site.urls),
]
