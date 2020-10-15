from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core import serializers
from bestdeals.kilimall import Scrape
from bestdeals.models import User, TrackedProduct, UserProduct
import json
import pprint

def home(request):
    scraper = Scrape()
    data = scraper.get_flashsales()
    scraper.save_to_db(data)
    tracked_products = TrackedProduct.objects.all()

    if request.method == 'POST' and 'track_button' in request.POST:
        data = request.POST
        print(data)

        # Process data from frontend
        products = data['products_to_track'].split(',')
        phone = data['user_phone']

        # Store data
        if User.objects.filter(user_phone=phone).exists():
            user = User.objects.get(user_phone=phone)

            for product in products:
                product_to_store = UserProduct(
                    user = user,
                    tracked_product = product
                )
                product_to_store.save()

        else:
            User.objects.create(user_phone=phone)
            user = User.objects.get(user_phone=phone)

            for product in products:
                product_to_store = UserProduct(
                    user = user,
                    tracked_product = product
                )
                product_to_store.save()
   
    return render(request, 'index.html', {'tracked_products': tracked_products})

def ajax(request):
    if request.method == 'POST':
        print('ajax')
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
        