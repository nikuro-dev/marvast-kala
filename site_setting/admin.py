from django.contrib import admin
from .models import SiteSetting, FooterLink, FooterLinkBox, Slider
# Register your models here.

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'footer_link_box']
    #list_editable = ['title', 'url', 'footer_link_box']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'button_url']
    #list_editable = ['title', 'button_url']





admin.site.register(SiteSetting)
admin.site.register(FooterLink, FooterLinkAdmin)
admin.site.register(FooterLinkBox)
admin.site.register(Slider, SliderAdmin)
