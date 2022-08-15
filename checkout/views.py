from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LX9oVD0kFC51IAOpvzx5sHKHj91I1c7m1EPifhhOgK2m3dj87HpOXHvTXzXSbwv9W1MemBb0BhyPeHTdDjexQCp00oyJDoLEG',
        'client_secret': 'sk_test_51LX9oVD0kFC51IAOpScmcCVe8wNYbhFlDEqpZXk5qFinq8peOtjW87E5kwyFBGQPK9hiWgQc468XumDc1b9ILu0r00opAimTGa',
    }

    return render(request, template, context)
