import pytest
from selenium.webdriver.common.by import By
from pages.gear_page.category_page import BasePage
from locators.base_page_locators import BasePageLocators

url_list = [
    'https://magento.softwaretestingboard.com/',
    'https://magento.softwaretestingboard.com/what-is-new.html',
    'https://magento.softwaretestingboard.com/women.html',
    'https://magento.softwaretestingboard.com/men.html',
    'https://magento.softwaretestingboard.com/gear.html',
    'https://magento.softwaretestingboard.com/training.html',
    'https://magento.softwaretestingboard.com/sale.html',
    'https://magento.softwaretestingboard.com/gear/bags.html',
    'https://magento.softwaretestingboard.com/gear/fitness-equipment.html',
    'https://magento.softwaretestingboard.com/gear/watches.html',
    'https://magento.softwaretestingboard.com/men/tops-men.html',
    'https://magento.softwaretestingboard.com/men/bottoms-men.html',
    'https://magento.softwaretestingboard.com/women/tops-women.html',
    'https://magento.softwaretestingboard.com/women/bottoms-women.html'
]

values_to_check = ['visibility', 'clickability'] # можно использовать данный список для отправки в  параметризацию, если нужно проверить два условия

@pytest.mark.parametrize("param", values_to_check)
@pytest.mark.parametrize("any_url", url_list)
def test_check_visibility_or_clickability_of_the_title_write_for_us(param,any_url,driver): 
    """
    TC_012.001.001 | Footer > "Write for us" link > Verify visibility of the link for the page for writing an article
        Steps:
            1. Open any page on The Site.
            2. Locate the Footer section.
            3. Verify the presence of the title "Write For Us" in the Footer.
        Expected results:
            The title "Write For Us" is visible in the footer of current page of The Site.

    TC_012.001.002 | Footer > "Write for us" link > Verify clickability of the link for the page for writing an article
        Precondition:
            The User is on any page The Site and the title "Write For Us" is presence in the footer.
        Steps:
             Check the ability to click on the link
        Expected results:
            The link is clickable"""
    
    expected_link = 'https://softwaretestingboard.com/write-for-us/' 

    any_page = BasePage(driver=driver,url=any_url)
    any_page.open()
    any_page.verify_visability_or_clickability_of_the_element_in_location(
        param=param,
        element_value=f"The link to the '{expected_link}'",
        element_locator=BasePageLocators.WRITE_FOR_US_LINK,
        location="the footer"
    )

@pytest.mark.parametrize("any_url", url_list)
def test_check_visibility_of_the_copyright(any_url,driver):
    """
    TC_012.011.001 | Footer > Self > Verify Copyright statement in the footer
        Steps:
            1. Open any page on the website.
            2. Locate the Footer section.
            3. Verify the presence of the copyright statement in the Footer.
        Expected results:
            The copyright information is visible in the footer of current page of the website."""
    
    # expected_text = "Copyright © 2013-present Magento, Inc. All rights reserved."
    any_page = BasePage(driver=driver,url=any_url)
    any_page.open()
    any_page.verify_visability_or_clickability_of_the_element_in_location(
        param="visibility",
        element_value="The copyright information",
        element_locator=BasePageLocators.COPYRIGHT_INFO,
        location="the footer"
    )
