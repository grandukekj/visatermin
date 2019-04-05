from selenium import webdriver
from functions import *

userinfos = load_userinfo()

# personal infos
GebJahr = userinfos['GebDatum'][:4]
GebMon = str(int(userinfos['GebDatum'][5:7]))
GebTag = str(int(userinfos['GebDatum'][8:]))

driver = webdriver.Chrome()
driver.get(
    "https://formular.berlin.de/xima-forms-29/get/14963116144270000?mandantid=/OTVBerlin_LABO_XIMA/000-01"
    "/instantiationTasks.properties")

# click on 'appointment change'
driver.find_element_by_xpath('//*[@id="btnTerminAendern"]').click()
# first name
driver.find_element_by_xpath('//*[@id="tfFirstName"]').send_keys(userinfos['vorname'])
# last name
driver.find_element_by_xpath('//*[@id="tfLastName"]').send_keys(userinfos['nachname'])
# birthdate: day
driver.find_element_by_xpath('//*[@id="cobGebDatumTag"]/option[@value=%s]' % GebTag).click()
# birthdate: month
driver.find_element_by_xpath('//*[@id="cobGebDatumMonat"]/option[@value=%s]' % GebMon).click()
# birthdate: year
driver.find_element_by_xpath('//*[@id="tfGebDatumJahr"]').send_keys(GebJahr)
# Vorgangsnummer
driver.find_element_by_xpath('//*[@id="tfVorgangsnummer"]').send_keys(userinfos['vorgangsnummer'])
# weiter
driver.find_element_by_xpath('//*[@id="txtNextpage"]').click()

newList = driver.find_elements_by_xpath('//*[@link="1"]')

if newList:
    send_gmailalert(userinfos['sender_email'], userinfos['sender_password'], userinfos['email_address'])
    driver.close()

else:
    driver.find_element_by_xpath('//*[@id="labnextMonth"]').click()
    newList = driver.find_elements_by_xpath('//*[@link="1"]')
    if newList:
        send_gmailalert(userinfos['sender_email'], userinfos['sender_password'], userinfos['email_address'])
        driver.close()
    else:
        driver.close()
