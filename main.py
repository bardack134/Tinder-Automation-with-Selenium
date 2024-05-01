from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import FACEBOOK_MAIL, FACEBOOK_PASSWORD

class TinderBot:
    def __init__(self):
        
        # Keep the browser open after the script has run, and expand the browser
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
                
        # Crear objeto webdriver para Chrome
        self.driver = webdriver.Chrome(options=chrome_options)

        #get the website
        self.driver.get(url="http://www.tinder.com")
        
        
    def web_navegate(self):
        """Method that enter on tinder website and looking for the sing in button"""
        
        try:
            sleep(2)
            #we get the 'login button and click on it'
            login_button=self.driver.find_element(By.CSS_SELECTOR, value="a.c1p6lbu0")
            login_button.click()

            #clik in the 'continue using Facebnook'
            sleep(4)
            continue_with_facebook=self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Log in with Facebook"]')
            continue_with_facebook.click()    



        except Exception as err:
            
            # print error message if the element was not found
            print(f"Error occurred while finding sign in element or 'continue using Facebook': {err}")  
            
            
    def cookies(self):
        """Methods that accept the cookies"""
        
        try:
            
            #5 seconds waiting until the page loads
            sleep(5)
            
            #We look for the 'I accept' button for cookies.
            cookie=self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
            cookie.click()
            
        except Exception as err:
            
            # print error message if the element was not found
            print(f"Error occurred while finding the 'I accept' cookie element:  {err}")      
   

    def user_name_password(self):
        """Method that enter on tinder the  provided email and password"""
        
        try:
            sleep(4)
            
            #switching from the base window to the new window to enter the email and password
            base_window = self.driver.window_handles[0]
            fb_login_window = self.driver.window_handles[1]
            self.driver.switch_to.window(fb_login_window)
            
            #print the driver.title to verify that it's the facebook login window that is currently target
            print(self.driver.title)
            
            #We look for the input boxes to enter the username and passwords
            sign_in_username=self.driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
            sign_in_username.send_keys(FACEBOOK_MAIL)
            sign_in_password=self.driver.find_element(By.ID, "pass")
            sign_in_password.send_keys(FACEBOOK_PASSWORD, Keys.ENTER)    
             
        except Exception as err:
            
            # Imprimir un mensaje de error si ocurre una excepción
            print(f"Error occurred while entering the username or password: {err}") 
                        
    def login(self):
        """Methods that manages the loging process"""
        self.cookies()
        self.web_navegate()
        self.user_name_password()
             
            
            
tinder_bot=TinderBot()

tinder_bot.login()