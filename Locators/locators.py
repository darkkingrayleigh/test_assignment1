class Locators():

    # Flipkart Home Page
    search_box_name = 'q'
    alert_close_button_xpath = '/html/body/div[2]/div/div/button'
    empty_value_class_name = '_3uTeW4'
    first_result_xpath = '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a'

    # Flipkart Product Page
    item_price_class_name = '_30jeq3'
    add_to_cart_xpath = '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button'
    increment_item_quantity_class_name = '_23FHuj'
    increment_item_quantity_xpath = '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/button[2]'
    item_pricex2_class_name = '_2-ut7f'
    stock_toast_class_name = '_2cf1Xf'
    flipkart_item_title_class_name = '_2Kn22P'
    flipkart_item_title = ''

    #Amazon Home Page
    search_box_id_amazon = 'twotabsearchtextbox'

    #Amazon Product Page
    item_price_xpath_amazon = '//*[@id="newAccordionRow"]/div/div[1]/a/h5/div[2]/div/span[1]'
    add_to_cart_id_amazon = 'add-to-cart-button'
    cart_button_id_amazon = 'attach-view-cart-button-form'
    checkout_price_xpath_amazon = '//*[@id="sc-subtotal-amount-buybox"]/span'