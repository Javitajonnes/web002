from .models import LinkSocial

def ctx_dict(request):
    #ctx={"test":"Soi un dato"}
    ctx={}
    link=LinkSocial.objects.all()
    for L in link:
        ctx[l.key]=l.url
    return ctx