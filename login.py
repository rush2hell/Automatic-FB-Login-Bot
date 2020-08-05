from selenium import webdriver
webpage = webdriver.Chrome()

webpage.get("https://facebook.com")

email = webpage.find_element_by_id("email")
email.send_keys("test@gmail.com")

password = webpage.find_element_by_id("pass")
password.send_keys("password")

login = webpage.find_element_by_id("u_0_b")
login.click()