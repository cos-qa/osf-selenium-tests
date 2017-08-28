'''
Created on Aug 22, 2017

@author: patrickanderson
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class Forks:

    def create_fork(self, driver):
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()='Forks']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()='New fork']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[text()='Fork']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[text()='Go to new fork']").click()
        time.sleep(3)
        return driver.current_url

    def create_fork_dashboard(self, driver):
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='overview']/div[1]/div[2]/div/div[2]/div/a/i").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='overview']/div[1]/div[2]/div/div[2]/div/ul/li[1]/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/button[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[text()='Go to new fork']").click()
        time.sleep(3)
        return driver.current_url