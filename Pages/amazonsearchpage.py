import re
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.locators import Locators


class AmazonSearchPage():

    def __init__(self, driver):
        self.driver = driver

    def compare_item(self, flipkart_item_title,flipkart_item_price):
        try:

            search_box = self.driver.find_element_by_id(Locators.search_box_id_amazon)
            search_box.clear()
            search_box.send_keys(flipkart_item_title)
            search_box.submit()

            time.sleep(5)
            title = re.sub('[^A-Za-z0-9\\s]+','', flipkart_item_title)

            pattern_list = title.split(" ")
            product_links = self.driver.find_elements_by_class_name('a-size-medium')
            relevant_link = ''
            relevance = 0
            for i in product_links:
                current_relevance = 0
                text = i.text.lower()
                if pattern_list[0].lower() in text:
                    for j in pattern_list:
                        if j.lower() in text:
                            current_relevance = current_relevance + 1

                    if current_relevance > relevance:
                        relevant_link = i.text
                        relevance = current_relevance

            if len(pattern_list) > relevance:
                return "Product is not available in Amazon"

            item_to_compare = self.driver.find_element_by_partial_link_text(relevant_link)
            item_to_compare.click()
            self.driver.switch_to.window(self.driver.window_handles[2])
            time.sleep(5)

            item_price = self.driver.find_element_by_xpath(Locators.item_price_xpath_amazon).text
            print("Price of item in Amazon is:", item_price, "Qty 1")

            self.driver.find_element_by_id(Locators.add_to_cart_id_amazon).click()

            time.sleep(5)
            self.driver.find_element_by_id(Locators.cart_button_id_amazon).click()

            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(((By.XPATH, Locators.checkout_price_xpath_amazon))))
            amazon_item_price = self.driver.find_element_by_xpath(Locators.checkout_price_xpath_amazon).text

            print("Price at checkout is: ₹", amazon_item_price, "Qty 1")
            amazon_item_price = amazon_item_price.replace(",", "")
            amazon_item_price = amazon_item_price.strip()
            amazon_item_price = int(float(amazon_item_price))

            flipkart_item_price = flipkart_item_price.replace(",", "")
            flipkart_item_price = flipkart_item_price.strip()
            flipkart_item_price = int(flipkart_item_price)

            if flipkart_item_price > amazon_item_price:
                print("This item is cheaper in Amazon")
            elif flipkart_item_price < amazon_item_price:
                print("This item is cheaper in Flipkart")
            else:
                print("Both Amazon and Flipkart have the same price")
            return "Success"

        except NoSuchElementException:
            return "Something went wrong"
        except TimeoutException:
            return "Something went wrong"