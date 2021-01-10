from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headlesss')
driver= webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/ganapatibhat/Documents/testing_frameworks/Selenium/Demo/chromedriver')
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://google.com')
print(driver.title)
driver.close()
driver.quit()

print('Test Completed')