from demo.models import Item
import stripe
from demo.serializers import ItemSerialaizer
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from django.shortcuts import render
from decouple import config

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerialaizer


def Item_ViewSet_id(request, pk):
    queryset = Item.objects.get(id=pk)
    stripe.api_key = config('Stripe_Api_key')
    session = stripe.checkout.Session.create(
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': f'{queryset.name}',
                    'description': f'{queryset.description}',
                },
                'unit_amount': queryset.price,
            },
            'quantity': 1,
        }],
        mode='payment',
    )
    return JsonResponse({'id': session.id})


def ItemViewSet_HTML(request, pk):
    queryset = Item.objects.get(id=pk)
    context = {
        'item': queryset.name,
        'description': queryset.description,
        'price': queryset.price,
        'id': pk
    }
    return render(request, 'demo.html', context)
