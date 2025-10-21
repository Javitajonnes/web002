from django.shortcuts import render,get_object_or_404
from .models import Category,MakeOrder

def myorder(request):
    makeorder=MakeOrder.objects.all()
    return render(request,"ot/listaOrdenes.html",
                  {'makeorder':makeorder})
def category(request,id_category): 
    ctg=Category.objects.get(id=id_category)
    makeorder=MakeOrder.objects.filter(categories=ctg)
    #ctg=get_object_or_404(Category,id_category)
    return render(request,"ot/categorias.html",
                  {"ctg":ctg,
                   'makeorder':makeorder})

