from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core import serializers
from bestdeals.kilimall import Scrape
from bestdeals.models import Flashsale, User, TrackedProduct
import json
import pprint

def home(request):
    tracked_products = TrackedProduct.objects.all()

    if request.method == 'POST':
        print(request.body)

        # user = User.objects.filter(user_phone=phone)
        # if int(phone[1:]) in [User.user_phone for User in user]:
        #     print('yeas')

        #     for each in tracked_item:
        #         tracked_product = TrackedProduct(
        #             user = user,
        #             tracked_product_name = each
        #         )

        # else:
        #     print('welcome new User') 
        #     new_user = User(
        #         user_phone = int(phone[1:])
        #     )  
        #     new_user.save()

        #     user = User.objects.filter(user_phone=phone)

        #     for each in tracked_item:
        #         tracked_product = TrackedProduct(
        #             user = user,
        #             tracked_product_name = each
        #         )

        #         tracked_product.save()

    # scrape = Scrape()
    # flashsales = scrape.get_flashsales()
    # scrape.save_to_db(flashsales)
   
    return render(request, 'index.html', {'tracked_products': tracked_products})

def ajax(request):
    if request.method == 'POST':
        print(request.body)
        print(request.POST)
        print(request.POST.get('phone'))
        print(request.POST.get('trackedItem'))
        # item = request.POST.get('track_item')
        # user = User.objects.get(user_name='Jaymoh')

        # response_data = {}

        # product = TrackedProduct(user=user, tracked_product_name=item)
        # product.save()

        # response_data['result'] = 'Create post successful!'
        # response_data['item'] = product.tracked_product_name        

        response_data = {'me': 3553}
        
        return JsonResponse(response_data)





    # else:
    #     return HttpResponse(
    #         json.dumps({"nothing to see": "this isn't happening"}),
    #         content_type="application/json"
    #     )
    
    # scrape = Scrape()
    # flashsales = scrape.get_flashsales()
    # scrape.save_to_db(flashsales)

    # Entices clients with Amazing deals from kilimall
    # best = Flashsale.objects.filter(product_price__lte=100) 
    # print(best)

    # register client
    

    # search = request.GET.get('search_product', '')
    # if search:
    #     products = Flashsale.objects.filter(product_descriptions__icontains=search).values
        