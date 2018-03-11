from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class AboutUs(TemplateView):

    template_name = "aboutus.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DynamicUrl(TemplateView):

    # template_name = "aboutus.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_template_names(self, **kwargs):
        print(self.args)
        return self.args[0] + ".html"