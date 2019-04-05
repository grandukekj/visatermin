from selenium import webdriver
from functions import *

userinfos = load_userinfo()

# personal infos
GebJahr = userinfos['GebDatum'][:4]
GebMon = str(int(userinfos['GebDatum'][5:7]))
GebTag = str(int(userinfos['GebDatum'][8:]))

# start the automation process
driver = webdriver.Chrome()
driver.get("https://formular.berlin.de/xima-forms-29/get/14963116144270000?mandantid=/OTVBerlin_LABO_XIMA/000-01"
           "/instantiationTasks.properties")

# click on "book an appointment" button
driver.find_element_by_xpath("//*[@id='btnTerminBuchen']").click()

# select my country
driver.find_element_by_xpath('//*[@id="cobStaat"]/option[@text="Korea, Republik"]').click()

# select whether you have familiy members to bring
driver.find_element_by_xpath('//*[@id="cobFamAngInBerlin"]/option[@text == "Nein"]').click()

# select anliegen as "arbeitsplatzs suche"
driver.find_element_by_xpath('//*[@id="cobAnliegen"]/option[@value="305245"]').click()

# agree to terms
driver.find_element_by_xpath('//*[@id="cbZurKenntnis"]').click()

# proceed to next page
driver.find_element_by_xpath('//*[@id="labNextpage"]').click()

# input Vorname and Nachname
driver.find_element_by_xpath('//*[@id="tfFirstName"]').send_keys(userinfos['vorname'])
driver.find_element_by_xpath('//*[@id="tfLastName"]').send_keys(userinfos['nachname'])

# select birth dates
driver.find_element_by_xpath('//*[@id="cobGebDatumTag"]/option[@text = %s]' % GebTag).click()
driver.find_element_by_xpath('//*[@id="cobGebDatumMonat"]/option[@text = %s]' % GebMon).click()
driver.find_element_by_xpath('//*[@id="tfGebDatumJahr"]').send_keys(GebJahr)

# select the number of applicants (eine Person)
VPers = driver.find_element_by_xpath('//*[@id="cobVPers"]/option[@text = "eine Person"]').click()

# input email address
driver.find_element_by_xpath('//*[@id="tfMail"]').send_keys(userinfos['email_address'])

# indicate whehter you have an existing visa (Ja, if visanummer exists. Nein, otherwise)

if userinfos['visanummer'] != '':  # D42340994

    driver.find_element_by_xpath('//*[@id="cobGenehmigungBereitsVorhanden"]/option[@text = "Ja"]').click()
    # input the visanummer of the existing visa
    driver.find_element_by_xpath('//*[@id="tfEtNr"]').send_keys(userinfos['visanummer'])

else:

    driver.find_element_by_xpath('//*[@id="cobGenehmigungBereitsVorhanden"]/option[@text = "Nein"]').click()

# proceed to next page
driver.find_element_by_xpath('//*[@id="txtNextpage"]').click()

# look for available dates
newList = driver.find_elements_by_xpath('//*[@link="1"]')

if newList:
    send_gmailalert(userinfos['sender_email'], userinfos['sender_password'], userinfos['email_address'])
    driver.close()

else:
    driver.close()
