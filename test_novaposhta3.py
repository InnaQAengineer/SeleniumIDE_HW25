# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNovaposhta3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_novaposhta3(self):
    self.driver.get("https://novaposhta.ua/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("мій акаунт")
    self.driver.find_element(By.CSS_SELECTOR, ".search > form > input").click()
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("кривий ріг")
    self.driver.find_element(By.XPATH, "//div[3]/div[2]/form/input").click()
    self.driver.find_element(By.LINK_TEXT, "Перенести доставку").click()
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("київ")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    text = self.driver.find_element(By.CSS_SELECTOR, ".text > h2").text
    assert text != "Мій"
  
