from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from core.models import Present
from core.views.payment_view import _mercado_pago_init_payment
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
            'present': present, 'key': settings.STRIPE_PUBLISHABLE_KEY
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        present = Present.objects.get(id=request.POST.get('pk'))
        return redirect(_mercado_pago_init_payment(present, request.POST.get('name'), request.POST.get('surname')))


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
