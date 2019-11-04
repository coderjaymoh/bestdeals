from django.shortcuts import render
from bestdeals.kilimall import Scrape
from bestdeals.models import Flashsale

def home(request):
    scrape = Scrape()
    flashsales = scrape.get_flashsales()
    scrape.save_to_db(flashsales)

    return render(request, 'home.html', {})
