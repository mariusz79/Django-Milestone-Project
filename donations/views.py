from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Donation
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.utils import timezone
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def donate(request):
    """view the donation form"""
    return render(request, 'donate.html', {'publishable': settings.STRIPE_PUBLISHABLE_KEY})

@login_required
def charge(request): 
    """donate money using stripe"""
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=int(request.POST.get('quantity'))*100,
            currency="EUR",
            description='A Django charge',
            source=request.POST['stripeToken']
        )

        #add user to the 'paid' group
        paid = Group.objects.get(name='paid')
        paid.user_set.add(request.user)

        #create and save instance of Donation model
        amount = int(request.POST.get('quantity'))
        donation = Donation()
        donation.sponsor = request.user
        donation.amount = amount
        donation.date = timezone.now()
        donation.save()
        return render(request, 'charge.html', {'amount': amount})
