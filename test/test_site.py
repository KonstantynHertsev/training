from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_s6 (browser):
    hompage = HomePage (browser)
    hompage.open()
    hompage.click_galaxy_s6()
    product_page = ProductPage (browser)
    product_page.check_title_is ('Samsung galaxy s6')
   


def test_two_monitors (browser):
    hompage = HomePage (browser)
    hompage.open()
    # browser.get ('https://www.demoblaze.com/')
    hompage.click_monitor()
    # monitor_link = browser.find_element (By.CSS_SELECTOR, value ='''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    time.sleep(2)
    hompage.check_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, value ='.card')
    #assert len(monitors) == 2

