import json

import stripe
import mercadopago
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from core.models import Present
from wedding import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def process_payment(request):

    data = json.loads(request.body)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'brl',
                'unit_amount': int(data['price'] * 100),
                'product_data': {
                    'name': data['name'],
                    'description': data['name'],
                },
            },  # Replace with your Stripe Price ID
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success', kwargs={})),
        cancel_url=request.build_absolute_uri(reverse('cancel', kwargs={}))
    )

    return JsonResponse({'id': session.id})


def payment(request, pk):
    present = Present.objects.get(id=pk)
    return redirect(_mercado_pago_init_payment(present))


def _mercado_pago_init_payment(present):

    sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    mercadopago_request = {
        "items": [
            {
                "id": "1234",
                "title": present.name,
                "description": present.description,
                "picture_url": f"https://tayseejunior.com.br{present.image.url}",
                "category_id": "Presente",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": present.price,
            },
        ],

        "back_urls": {
            "success": "https://tayseejunior.com.br/success",
            "failure": "https://tayseejunior.com.br/cancel",
            "pending": "https://tayseejunior.com.br/success",
        },
        "auto_return": "all",
        "external_reference": present.id,

    }

    preference_response = sdk.preference().create(mercadopago_request)
    preference = preference_response["response"]

    print(preference)
    return preference['init_point']


def webhook(request):
    print(request)
    return JsonResponse({'body': request.body})
