from selenium import webdriver
from bestdeals.models import Flashsale
import pprint

class Scrape:
    driver = webdriver.Chrome('/home/jaymoh/projects/personal/selenium/bestdeals/chromedriver')

    # scraped and foomatted
    def get_flashsales(self):
        driver = self.driver
        # flashsale_url = 'file:///home/jaymoh/projects/personal/selenium/bestdeals/Flash%20Sale%20_%20Kilimall.html'
        flashsale_url = 'https://www.kilimall.co.ke/new/flash-sales'
        driver.get(flashsale_url)
        flashsale_products = []
        formatted_flashsale_products = []

        for each in driver.find_elements_by_css_selector('div.goods_item'):
            print(each.text)
        
            flashsale_products.append(each.text)

        for each in flashsale_products:
            formatted_flashsale_products.append(each.split('\n'))

        pprint.pprint(formatted_flashsale_products)
        driver.close()

        return formatted_flashsale_products

    def save_to_db(self, formatted_flashsale_products):
        for each in formatted_flashsale_products:
            flashsales_save = Flashsale(
                product_descriptions = each[0],
                products_left = each[1],
                product_price = each[2],
                cash_saved = each[3]
            )

            flashsales_save.save()
