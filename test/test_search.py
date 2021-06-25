import time
import unittest
from selenium import webdriver

from Pages.amazonsearchpage import AmazonSearchPage
from Pages.searchpage import SearchPage


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_search_flipkart(self):
        search_term = "Vu tv"

        self.driver.get("https://www.flipkart.com/")
        try:
            search = SearchPage(self.driver)

            search.alert_dismiss()

            search_item = search.search_term(search_term)
            self.assertEqual(search_item, "Search complete", "Search result was empty")

            price = search.select_product()
            self.assertNotEqual(price, "item is out of stock", "Item is out of stock")
            print("Price of the item is: ₹", price, "Qty 1")

            cart_item = search.check_cart_status()
            self.assertNotEqual(cart_item, "Unable to add to cart", "Unable to add item to cart")

            increment_product = search.increment_item()
            self.assertNotEqual(increment_product, "There is only one item available")

            print("Price of the item is: ₹", increment_product, "Qty 2")
        except AssertionError as e:
            print(e)
            raise


    def test_compare(self):
        compare_item_title = 'OPPO A54'
        self.driver.get("https://www.flipkart.com/")
        try:
            search = SearchPage(self.driver)
            search.alert_dismiss()

            flipkart_search_term = search.search_term(compare_item_title)
            self.assertEqual(flipkart_search_term, "Search complete", "Search result was empty")

            price = search.select_product()
            self.assertNotEqual(price, "item is out of stock", "Item is out of stock")
            print("Price of the item is: ₹", price, "Qty 1")

            flipkart_item_title = search.get_item_title()
            self.assertNotEqual(flipkart_item_title, "Unable to find the product title")

            cart_item = search.check_cart_status()
            self.assertNotEqual(cart_item, "Unable to add to cart", "Unable to add item to cart")
            print("Price of the item is: ₹", price, "Qty 1")

            time.sleep(5)

            compare = AmazonSearchPage(self.driver)
            self.driver.get("https://www.amazon.in/")

            compare_message = compare.compare_item(flipkart_item_title,price)
            self.assertEqual(compare_message, "Success", "Something went wrong")
        except AssertionError as e:
            print(e)
            raise
        except:
            raise

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()