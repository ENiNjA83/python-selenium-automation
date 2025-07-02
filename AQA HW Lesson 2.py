from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


#1) PRACTICE WITH LOCATORS for these page elements of Amazon Sign in page:

#Amazon logo, search by XPATH
driver.find_element(By.XPATH, '//[@role="img"]')
#Email field, search by ID
driver.find_element(By.ID, 'ap_email_login')
#Continue button, search by ID
driver.find_element(By.ID, 'continue')
#Conditions of use, search by partial path using XPATH
driver.find_element(By.XPATH, '//a[contains(@href, "ref=ap_signin_notification_condition_of_use")]')
#Privacy Notice link, search by partial match using XPATH
driver.find_element(By.XPATH, '//a[contains(@href, "ref=ap_signin_notification_privacy_notice")]')
#Need help link, search by partial match using XPATH
driver.find_element(By.XPATH, '//a[contains(@href, "ref=unified_claim_collection")]')
##"Forgot your password link" does not display on my page (see screenshot)
##"Other issues with Sign-in" does not display on the page (see screenshot)
#Create a free Business account button, search by text using XPATH
driver.find_element(By.XPATH, '//a[text()="Create a free Business account"]')

#2)Create a test case for the SignIn page using python & selenium script.
#1. Open https://www.target.com/
driver.get('https://www.target.com/')
sleep(3)

#2. Click Account button
driver.find_element(By.ID, 'account-sign-in').click()
sleep(3)

#3. Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(3)

#4. Verify SignIn page opened:
#“Sign in or create account” text is shown,
driver.find_element(By.XPATH, "//a[text()='Sign in or create account']")

#SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.ID, 'login')

print('Test case passed')
driver.quit()