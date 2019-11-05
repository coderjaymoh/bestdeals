from django.shortcuts import render
from bestdeals.kilimall import Scrape
from bestdeals.models import Flashsale

def home(request):
    scrape = Scrape()
    flashsales = scrape.get_flashsales()
    scrape.save_to_db(flashsales)

    # best = Flashsale.objects.filter(product_price__lte=100)
    # print(best)
    # search = request.GET.get('search_product', '')
    # if search:
    #     products = Flashsale.objects.filter(product_descriptions__icontains=search).values
        
         


    return render(request, 'home.html', {})
