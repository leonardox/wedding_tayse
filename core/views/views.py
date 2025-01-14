from django.views.generic import TemplateView

from core.models import Present
from wedding import settings


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)


class AboutView(TemplateView):
    template_name = 'common/about.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)


class MailView(TemplateView):
    template_name = 'message/mail.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)


class PresentListView(TemplateView):
    template_name = 'presents/presents.html'

    def get(self, request, *args, **kwargs):
        presents = Present.objects.all()
        context = {
            'some_dynamic_value': 'This text comes from django view!', 'presents': presents
        }
        return self.render_to_response(context)


class PresentView(TemplateView):
    template_name = 'presents/present_detail.html'

    def get(self, request, *args, **kwargs):
        present = Present.objects.get(pk=kwargs['pk'])
        context = {
            'some_dynamic_value': 'This text comes from django view!', 'present': present, 'key': settings.STRIPE_PUBLISHABLE_KEY
        }
        return self.render_to_response(context)


class SuccessView(TemplateView):
    template_name = 'payment/success.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)


class CalcelView(TemplateView):
    template_name = 'payment/cancel.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)
