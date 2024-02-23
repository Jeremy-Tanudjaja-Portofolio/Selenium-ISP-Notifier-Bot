from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium import webdriver
import time


class InternetBot:
    def __init__(self):
        # chrome_driver = Service(r"D:\Development res\Chrome Driver\chromedriver.exe")
        self.download_speed = None
        self.upload_speed = None
        self.provider_name = None
        self.driver_path = "D:\Development res\Chrome Driver\chromedriver.exe"
        self.get_internet_speed()

    def get_internet_speed(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get("https://www.speedtest.net/")
        time.sleep(10)
        click = driver.find_element(By.CLASS_NAME, "js-start-test")
        click.click()
        time.sleep(45)  # Making sure the page finishes loading first
        self.download_speed = float(driver.find_element(By.CLASS_NAME, "download-speed").get_attribute("innerHTML"))
        self.upload_speed = float(driver.find_element(By.CLASS_NAME, "upload-speed").get_attribute("innerHTML"))
        self.provider_name = driver.find_element(By.CLASS_NAME, "js-data-isp").get_attribute("innerHTML")
        # print(f"{self.download_speed}, {self.upload_speed}, {self.provider_name}")



    def contact_provider_twitter(self):
        # To Contact Twitter Account
        driver = webdriver.Chrome(self.driver_path)
        driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        #Entering Email
        text_input = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        text_input.send_keys("user@gmail.com")
        click = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        click.click()
        time.sleep(5)

        # Entering username
        username_input = driver.find_element(By.XPATH,
                                         "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        username_input.send_keys("Username name")
        click_username = driver.find_element(By.XPATH,
                                    "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
        click_username.click()
        time.sleep(5)

        #Entering Password
        password = driver.find_element(By.NAME, "password")
        password.send_keys(r"password credential")
        click_password = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        click_password.click()
        time.sleep(5)

        #Making a Tweet
        tweet = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span/br")
        tweet.send_keys(f"Hello Internet Provide, my Internet Speed is suboptimal as per our contract\n Download: {self.download_speed}\n Upload:{self.upload_speed}")
        send_tweet = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
        send_tweet.click()