import time

link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_should_be_button_add_to_basket_on_page(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert button, 'button "add to basket" not found on page'



