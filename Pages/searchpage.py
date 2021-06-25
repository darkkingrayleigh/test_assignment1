import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import Locators

from Locators.locators import Locators


class SearchPage():

    def __init__(self, driver):
        self.driver = driver

    def alert_dismiss(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locators.alert_close_button_xpath)))
            alert.click()
        except NoSuchElementException:
            pass

    def search_term(self, term):
        search_field = self.driver.find_element_by_name(Locators.search_box_name)
        search_field.clear()
        search_field.send_keys(term)
        search_field.submit()

        try:
            empty_search = self.driver.find_element_by_class_name(Locators.empty_value_class_name)
            if empty_search == 'Sorry, no results found!':
                return "Search result is empty"

        except NoSuchElementException:
            return "Search complete"

    def select_product(self):
        first_item = self.driver.find_element_by_xpath(Locators.first_result_xpath)
        first_item.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        price = self.driver.find_element_by_class_name(Locators.item_price_class_name).text[1:]
        try:
            cart_button = self.driver.find_element_by_xpath(Locators.add_to_cart_xpath)
            time.sleep(5)
            cart_button.click()
            return price

        except NoSuchElementException:
            return "item is out of stock"

    def check_cart_status(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, Locators.stock_toast_class_name)))
            cart_status = self.driver.find_element_by_class_name(Locators.stock_toast_class_name).text
            if "Unable to add to Cart" in cart_status:
                return "Unable to add to cart"
            else:
                return ""
        except NoSuchElementException:
            return ""
        except TimeoutException:
            return ""


    def increment_item(self):

        add_quantity = self.driver.find_element_by_xpath(Locators.increment_item_quantity_xpath)
        time.sleep(5)
        add_quantity.click()

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, Locators.stock_toast_class_name)))
        quantity = self.driver.find_element_by_class_name(Locators.stock_toast_class_name).text

        if "Sorry!" in quantity:
            return "There is only one item available"
        else:
            pricex2 = self.driver.find_element_by_class_name(Locators.item_pricex2_class_name).text[1:]
            return pricex2

    def get_item_title(self):
        try:
            flipkart_item_title = self.driver.find_element_by_class_name(Locators.flipkart_item_title_class_name).text
            return flipkart_item_title
        except NoSuchElementException:
            return "Unable to find the product title"









