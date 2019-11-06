from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from bestdeals.kilimall import Scrape
from bestdeals.models import Flashsale, Client, TrackedProduct
from bestdeals.forms import ClientForm
import json
import pprint

def home(request):
    if request.method == 'POST':
        print(request.POST)
        item = request.POST.get('the_post')
        print(item)
        client = Client.objects.get(client_name='kish')

        response_data = {}

        product = TrackedProduct(client=client, tracked_product_name=item)
        product.save()

        response_data['result'] = 'Create post successful!'
        response_data['item'] = product.tracked_product_name

        # Get previously stored tracked products
        tracked_products = TrackedProduct.objects.all()
        jsoned_data = serializers.serialize('json', list(tracked_products.tracked_product_name), fields=('tracked_product_name',))
        pprint.pprint(jsoned_data)

        context = {
            'response_data': response_data,
            'tracked_products': tracked_products
        }

        return JsonResponse(context)

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
        
         


    return render(request, 'index.html', {})

def signup(request):
    if request.method == 'POST':
        form = ClientForm(request.POST or None)
        if form.is_valid:
            form.save()
            
            return redirect('signup')
        
        else:
            return redirect('home')

    else:
        form = ClientForm

    return render(request, 'signup.html', {'form': form})