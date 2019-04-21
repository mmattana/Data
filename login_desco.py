from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#download Chrome drive and install at /usr/local/bin from https://sites.google.com/a/chromium.org/chromedriver/downloads
browser = webdriver.Chrome()

browser.get('https://descomplica.com.br/entrar/?cat=vestibulares')
login = input('Digite seu login')
senha = input('Agora sua senha')
elements = browser.find_elements_by_css_selector('.ds-new-login-signup-input')
elements[0].send_keys(login)
elements[1].send_keys(senha)
submit = browser.find_element_by_css_selector('.ds-new-login-submit-button')
submit.click()
