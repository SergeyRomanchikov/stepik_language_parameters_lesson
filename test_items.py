import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_add_button_exists(browser):
    def is_element_exists(xpath):
        try:
            element = browser.find_element_by_xpath(xpath)
            return element
        except NoSuchElementException:
            return False

    browser.get(link)
    time.sleep(30)
    add_to_basket_button_xpath = '//button[contains (@class, "add-to-basket")]'
    assert is_element_exists(add_to_basket_button_xpath), "Add to basket button not found"

