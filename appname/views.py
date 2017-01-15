import django.views.generic

class Home(django.views.generic.TemplateView):
    template_name = "home.html"
home = Home.as_view()