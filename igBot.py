from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Victor\\Desktop\\geckodriver_win\\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        ##Aumentar tempo de espera, caso o navegador seja lento. dentro do time.sleep(aqui)
        time.sleep(3)
        input_user = driver.find_element_by_xpath("//input[@name='username']")
        input_user.click()
        input_user.clear()
        input_user.send_keys(self.username)
        input_password = driver.find_element_by_xpath("//input[@name='password']")
        input_password.click()
        input_password.clear()
        input_password.send_keys(self.password)
        input_password.send_keys(Keys.RETURN)
        time.sleep(5)
        self.link()
        ##Colocar o @ da pessoa no checked_user
        checked_user = "@Heitorcassimiro"
        
        driver.find_element_by_class_name("Ypffh").click()
        comment_input_box = driver.find_element_by_class_name("Ypffh")
        self.comment_publish(checked_user,comment_input_box)
        driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()

       

    def link(self):
        driver = self.driver
    ## Por a URL da publicação no driver.get("Aqui")
        driver.get("https://www.instagram.com/p/CM2J9qFhbRN/")

    def comment_publish(self, comments, localBox):
     ##Comentando letra por letra   
        for letter in comments:
            localBox.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)
        
        
     

##colocar o login e senha respectivamente dentro das aspas 
victorBot = instagramBot('aqui','aqui')
victorBot.login()