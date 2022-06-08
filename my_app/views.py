
from django.shortcuts import render
from django.http import HttpResponse
#from django_daraja.mpesa.core import MpesaClient
from django.urls import reverse
from django_daraja_app.mpesa.core import MpesaClient


def index(request):
    cl = MpesaClient()
    stk_push_callback_url = 'https://darajambili.herokuapp.com/express-payment'
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0715806276'
    amount = 1
    account_reference = 'StartBox'
    transaction_desc = 'Description'
    #callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    callback_url = stk_push_callback_url

    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
    data = request.body
    print("The data is:", data)
    return HttpResponse(data)

        # You can do whatever you want with the notification received from MPESA here.


        