from django.contrib import admin
from .models import LinkSocial

class LinkSocialAdmin(admin.ModelAdmin):
    pass


admin.site.register(LinkSocial,LinkSocialAdmin)