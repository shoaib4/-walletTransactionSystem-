from django.shortcuts import render
from django.http import HttpResponse
from .models import WalletUser
# from Wallet.models import Wallet
# Create your views here.


def create_user(x):
    user = WalletUser.objects.create(name=x.get('name'))
    # wallet = Wallet.objects.create(amount=0)
    # user.wallet_uuid = wallet.uuid
    user.save()