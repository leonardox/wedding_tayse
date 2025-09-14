"""wedding01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin

from core.views import payment_view
from core.views.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="index"),
    path('gallery/', GalleryView.as_view(), name="gallery"),
    path('mail/', MailView.as_view(), name="mail"),
    path('presents/', PresentListView.as_view(), name="presents"),
    path('present/<int:pk>', PresentView.as_view(), name="present"),
    path('about/', AboutView.as_view(), name="about"),
    path('success/', SuccessView.as_view(), name="success"),
    path('cancel/', CancelView.as_view(), name="cancel"),
    path('create_checkout_session/', payment_view.process_payment, name='create_checkout_session'),
    path('payment/<int:pk>', payment_view.payment, name="payment"),
    path('webhook/', payment_view.webhook, name="webhook"),
    path('indicacoes', IndicationsView.as_view(), name="indications"),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
