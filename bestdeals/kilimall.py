from selenium import webdriver
from bestdeals.models import ScrapedProduct
import pprint

class Scrape:
    # scraped and formatted
    def get_flashsales(self):
        driver = webdriver.Chrome('/home/jaymoh/projects/personal/selenium/bestdeals/chromedriver')
        # driver = self.driver
        # flashsale_url = 'file:///home/jaymoh/projects/personal/selenium/bestdeals/Flash%20Sale%20_%20Kilimall.html'
        flashsale_url = 'https://www.kilimall.co.ke/new/flash-sales'
        driver.get(flashsale_url)
        driver1 = driver.find_elements_by_css_selector('b.memo')
        flashsale_products = []
        formatted_flashsale_products = []

        # Removed clicking of button
        # for each in driver.find_elements_by_css_selector('b.memo'):
            # if each.text == 'On Going':
            # each.click()

        for each in driver.find_elements_by_css_selector('div.goods_item'):        
            flashsale_products.append(each.text)

        for each in flashsale_products:
                formatted_flashsale_products.append(each.split('\n'))

        # pprint.pprint(formatted_flashsale_products)
        driver.close()

        return formatted_flashsale_products

    # Saving to db
    def save_to_db(self, formatted_flashsale_products):
        print(formatted_flashsale_products)
        for each in formatted_flashsale_products:
            # pprint.pprint(each)
            description = each[0] 
            left = each[1].split()[0] 
            price = each[2].split()[1] 
            saved = each[3].split()[2] 

            print(description,left,price,saved)

            # if ',' in each[2]: 
            #     product_price = each[1].replace(',','').split()[1]
            
            # else:
            #     product_price = each[1].split()[1]
            
            # if ',' in each[2]:
            #     cash_saved = each[2].replace(',','').split()[2]

            # else:
            #     product_price = each[2].split()[2]

            products = ScrapedProduct(
                product_descriptions = each[0],
                products_left = left,
                product_price = price,
                cash_saved = saved
            )

            products.save()

        return None