from django.db import models

class LinkSocial(models.Model):
    key=models.SlugField(verbose_name="Nombre Clave",unique=True)
    name=models.CharField(verbose_name="nombre",max_length=100)
    url=models.URLField(verbose_name="enlace",null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="F.Creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="F.Edicion")

    class Meta():
        verbose_name="enlace"
        verbose_name_plural="enlaces"

    def __str__(self):
        return self.name
        
