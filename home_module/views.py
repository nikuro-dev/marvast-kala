from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_setting.models import SiteSetting, FooterLinkBox, Slider
# Create your views here.

class HomeView(TemplateView):
    template_name = "home_module/index.html"
    model = SiteSetting
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter()

        return context

class AboutusView(TemplateView):
    template_name = "home_module/about_us.html"
    

class ContactusView(TemplateView):
    template_name = "home_module/contact_us.html"

def site_header_component(request):
    return render(request, "shared/site_header_component.html")


def site_footer_component(request):
    return render(request, "shared/site_footer_component.html")
