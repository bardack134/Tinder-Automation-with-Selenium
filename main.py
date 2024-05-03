from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants import FACEBOOK_MAIL, FACEBOOK_PASSWORD, PHONE_NUMBER

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

            #clik in the 'continue using facebook'
            sleep(3)
            continue_with_facebook=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button')
            continue_with_facebook.click()    



        except Exception as err:
            
            # print error message if the element was not found
            print(f"Error occurred while finding sign in element or 'continue using Google': {err}")  
            
            
    def cookies(self):
        """Methods that accept the cookies"""
        
        try:
            
            #5 seconds waiting until the page loads
            sleep(4)
            
            #We look for the 'I accept' button for cookies.
            cookie=self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
            cookie.click()
            
        except Exception as err:
            
            # print error message if the element was not found
            print(f"Error occurred while finding the 'I accept' cookie element:  {err}")      
   

    def user_name_password(self):
        """Method that enter on tinder the  provided email and password"""
        
        try:
            sleep(3)
            
            #NOTE:SWITCHING FROM THE BASE WINDOW TO THE NEW WINDOW TO ENTER THE EMAIL AND PASSWORD
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
                        
        else: 
            #Click in the 'yes, continue' to continue after enter the username, password and 'enter'           
            try: 
                sleep(5)   
                
                continue_button=self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div/div/div/form/div/button')
                
    
            except Exception as err:
                # If the 'continue' button is not found, do nothing
                print('Continue button not found. Proceeding without clicking')   
            
            else:
                continue_button.click()
        
        sleep(4)    
        #Switch back to main Tinder window
        self.driver.switch_to.window(base_window)
        
        #printing the window title to verify that is working and we are in the correct window
        print(self.driver.title)    
        
        
    def enter_phone_number(self):
        """this method enters the phone number, this method is use after user has login with username and password"""
        
        try:
            
            #3 seconds waiting until the page loads
            sleep(4)
            
            #We look for the 'I accept' button for cookies.
            phone_number_input=self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/input')
            phone_number_input.send_keys(PHONE_NUMBER)
            
            sleep(2)
            
            #click button 'next' after enter phone number
            next_button=self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div[3]/button')
            next_button.click()
            #NOTE: IN THIS PART THEY SEND A CONFIRMATION CODE TO CELLPHONE THAT WE NEED TO ENTER MANUALLY AFTER THAT WAIT FOR THE PROGRAMM CONTINUE
            sleep(14)
            
            next_button2=self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div[4]/button')
            next_button2.click()
        except Exception as err:
            
            # print error message if the element was not found
            print(f"Error occurred while entering the phone number or clicking button next:  {err}")        
                  
        
        
        
                                    
    def run_script(self):
        """Methods that manages the loging process"""
        self.cookies()
        self.web_navegate()
        self.user_name_password()
        self.enter_phone_number()     
            
            
tinder_bot=TinderBot()

tinder_bot.run_script()