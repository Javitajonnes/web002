from django.contrib import admin
from django.urls import path
from ot import views as views_ot

urlpatterns = [
    path('category/<int:id_category>/',views_ot.category,name="category"),
    path('list/',views_ot.myorder,
         name="list"),
    path('admin/', admin.site.urls),
]
