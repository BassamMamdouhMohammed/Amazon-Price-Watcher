from pages.home_page import HomePage
import time

def test_product_details(browser):
    """Verify that product details are displayed correctly."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    home.click_submit()
    home.search_product("Logitech Mouse")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    search.open_product_by_index(1)
    product = search.go_to_product_page()
    time.sleep(2)
    title = product.get_product_title()
    print(f"Product title is: {title}")
    price = product.get_price()
    print(f"Product Price is: {price} $")
    availability = product.get_availability()
    print(f"This Product is: {availability}")
    # Assertions to verify that product details are not empty   
    assert title != "", "Product title should not be empty"
    assert price != "", "Product price should not be empty"
    assert availability != "", "Product availability should not be empty"

def test_multiple_product_details(browser):
    """Verify that product details are displayed correctly."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    # home.click_submit()
    home.search_product("Logitech Mouse")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    search.open_product_by_review()
    product = search.go_to_product_page()
    time.sleep(2)
    title = product.get_product_title()
    print(f"Product title is: {title}")
    price = product.get_price()
    print(f"Product Price is: {price} $")
    availability = product.get_availability()
    print(f"This Product is: {availability}")
    # Assertions to verify that product details are not empty   
    assert title != "", "Product title should not be empty"
    assert price != "", "Product price should not be empty"
    assert availability != "", "Product availability should not be empty"

def test_get_multiple_products(browser):
    """Verify that multiple products can be retrieved from search results."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    # home.click_submit()
    home.search_product("Logitech Mouse")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    products = search.get_search_results()
    print(f"Number of products found: {len(products)}")
    # Assertion to verify that at least one product is found
    assert len(products) > 0, "No products found in search results"

def test_get_best_five_products(browser):
    """Verify that the best five products can be retrieved from search results."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    # home.click_submit()
    home.search_product("Logitech Mouse")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    products = search.get_search_results()
    print(f"Number of products found: {len(products)}")
    # Print details of the best five products
    for i in range(min(5, len(products))):
        product = products[i]
        title = product.text
        print(f"Product {i+1}: {title}")
    # Assertion to verify that at least five products are found
    assert len(products) >= 5, "Less than five products found in search results"

def test_add_to_cart(browser):
    """Verify that adding a product to the cart updates the cart count."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    # home.click_submit()
    home.search_product("Logitech Mouse")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    search.open_product_by_index(1)
    product = search.go_to_product_page()
    time.sleep(2)
    initial_cart_count = product.get_cart_count()
    print(f"Initial cart count: {initial_cart_count}")
    product.add_to_cart()
    time.sleep(2)  # Wait for cart update
    updated_cart_count = product.get_cart_count()
    print(f"Updated cart count: {updated_cart_count}")
    # Assertion to verify that the cart count has increased by 1
    assert updated_cart_count == initial_cart_count + 1, "Cart count should increase by 1 after adding a product"

def test_buy_now(browser):
    """Verify that clicking 'Buy Now' redirects to the sign-in page."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    # home.click_submit()
    home.search_product("Logitech Mouse")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    search.open_product_by_index(1)
    product = search.go_to_product_page()
    time.sleep(2)
    product.Buy_now()
    time.sleep(2)  # Wait for redirection
    # Assertion to verify that the current URL is the sign-in page
    assert "signin" in browser.current_url, "Should be redirected to the sign-in page after clicking 'Buy Now'"

def test_no_results_message(browser):
    """Verify that searching for a non-existent product shows the no results message."""
    home = HomePage(browser)
    home.open("https://www.amazon.com")
    # home.click_submit()
    home.search_product("asdasdasdasdasdasd")
    # Verify that search results are displayed  
    search = home.go_to_search_results_page()
    assert search.has_no_results_message(), "No results message should be displayed for a non-existent product"

