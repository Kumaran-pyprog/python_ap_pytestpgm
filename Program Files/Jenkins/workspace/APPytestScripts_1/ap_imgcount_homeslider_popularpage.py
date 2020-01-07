from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import pytest

import time

# TestCase-3
@pytest.mark.smoke
@pytest.mark.regression
def test_ap_gridimg_count_popular_bookseller_homeslider():
    global driver
    # Instantiate web browser
    driver = webdriver.Chrome()
    # browser should be loaded in maximized window
    driver.maximize_window()
    # driver should wait impicitly for a given duration ,for the element under the considertaion to load.
    # we will use built-in implicitly_wait() of our driver projects
    driver.implicitly_wait(10)  # 10 sec
    # to load given url in the browser window
    driver.get('http://automationpractice.com/index.php')

    # Navigate the poular menu and click the button
    driver.find_element_by_xpath('//ul[@id="home-page-tabs"]/li[1]/a').click()
    # Finding the No of Grid items in Popular menu Using xpath locator
    webelement_popular = driver.find_elements_by_xpath("//ul[@id='homefeatured']/li")
    lenof_griditems_popular = len(webelement_popular)
    # display the No of images present in popular menu
    print("No of images present in popular :", lenof_griditems_popular)
    time.sleep(2)

    # Navigate the poular menu and click the button
    driver.find_element_by_xpath('//ul[@id="home-page-tabs"]/li[2]/a').click()
    # Finding the No of Grid items in Bookseller menu Using xpath locator
    webelement_bestseller = driver.find_elements_by_xpath('//ul[@id="blockbestsellers"]/li')
    # display No of image present in bestseller
    lenof_griditems_bookseller = len(webelement_bestseller)
    print("No of images present in Bookseller :", lenof_griditems_bookseller)

    # Automate the homeslider images and find the no of images in the Homeslider
    driver.find_element_by_xpath('//ul[@id="homeslider"]')
    webelement_homeslider = driver.find_elements_by_xpath('//ul[@id="homeslider"]/li/a')
    # find the length of the homeslider images
    lengthof_homeslider = len(webelement_homeslider)
    print('No of images present in homslider :', lengthof_homeslider)

    # Automating the buttons previous and back
    driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]')
    driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]/div')
    homeslider_butnnext = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]/div/a[2]'))
    homeslider_butnnext.click()
    time.sleep(2)

    homeslider_butnprev = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]/div/a[1]'))
    homeslider_butnprev.click()

    # Automate the homecontent and find the no of image in the homecontent
    driver.find_element_by_xpath('//ul[@class="htmlcontent-home clearfix row"]')
    webelement_homecontent = driver.find_elements_by_xpath('//ul[@class="htmlcontent-home clearfix row"]/li')
    # find the length of the homecontent images
    lengthof_homecontent = len(webelement_homecontent)
    print("No of images present in homecontent :", lengthof_homecontent)

    # close the driver
    driver.close()
