from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from userInfo import *
from emailAlert import *
import time
import os

userinfos = load_userinfo()

# personal infos
GebJahr = userinfos.gebDatum[:4]
GebMon = userinfos.gebDatum[5:7]
GebTag = userinfos.gebDatum[8:]

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chromedriver = os.getcwd() + '/buchen/chromedriver.exe'

# driver = webdriver.Chrome(executable_path=chromedriver,   chrome_options=chrome_options)


try:
    # start the automation process

    driver = webdriver.Chrome()
    driver.get("https://formular.berlin.de/xima-forms-29/get/14963116144270000?mandantid=/OTVBerlin_LABO_XIMA/000-01"
               "/instantiationTasks.properties")

    # click on "book an appointment" button
    driver.find_element_by_xpath("//*[@id='btnTerminBuchen']").click()

    # select my country
    driver.find_element_by_xpath('//select[@id="cobStaat"]/option[text() = "Korea, Republik"]').click()
    # select whether you have familiy members to bring
    driver.find_element_by_xpath('//select[@id="cobFamAngInBerlin"]/option[text() = "Nein"]').click()

    # select anliegen as "arbeitsplatzs suche"
    driver.find_element_by_xpath('//select[@id="cobAnliegen"]/option[@value="305245"]').click()

    # agree to terms
    driver.find_element_by_xpath('//*[@id="cbZurKenntnis"]').click()

    # proceed to next page
    driver.find_element_by_xpath('//*[@id="labNextpage"]').click()

    # input Vorname and Nachname
    driver.find_element_by_xpath('//*[@id="tfFirstName"]').send_keys(userinfos.vorname)
    driver.find_element_by_xpath('//*[@id="tfLastName"]').send_keys(userinfos.nachname)
    #
    # # select birth dates
    driver.find_element_by_xpath('//select[@id="cobGebDatumTag"]/option[text() = %s]' % GebTag).click()
    driver.find_element_by_xpath('//select[@id="cobGebDatumMonat"]/option[text() = %s]' % GebMon).click()
    driver.find_element_by_xpath('//*[@id="tfGebDatumJahr"]').send_keys(GebJahr)

    # # select the number of applicants (eine Person)
    VPers = driver.find_element_by_xpath('//select[@id="cobVPers"]/option[text() = "eine Person"]').click()
    #
    # input email address
    driver.find_element_by_xpath('//*[@id="tfMail"]').send_keys(userinfos.emailAddress)

# indicate whehter you have an existing visa (Ja, if visanummer exists. Nein, otherwise)

    if hasattr(userinfos, 'visanummer') == 1: # D42340994

        driver.find_element_by_xpath('//select[@id="cobGenehmigungBereitsVorhanden"]/option[text() = "Ja"]').click()
        # input the visanummer of the existing visa
        driver.find_element_by_xpath('//*[@id="tfEtNr"]').send_keys(userinfos.visanummer)

    else:

        driver.find_element_by_xpath('//select[@id="cobGenehmigungBereitsVorhanden"]/option[text() = "Nein"]').click()

    # proceed to next page
    driver.find_element_by_xpath('//*[@id="txtNextpage"]').click()

    # look for available dates
    newList = driver.find_elements_by_xpath('//*[@link="1"]')

    if newList:
        send_gmailalert(userinfos.sender_email, userinfos.sender_password, userinfos.email_address)
        print 'found an appointment'
        driver.close()

    else:
        driver.find_element_by_xpath('//*[@id="labnextMonth"]').click()
        newList = driver.find_elements_by_xpath('//*[@link="1"]')
        if newList:
            send_gmailalert(userinfos['sender_email'], userinfos['sender_password'], userinfos['email_address'])
            driver.close()
        else:
            time.sleep(10)
            print 'try next time'
            driver.close()

except:
    time.sleep(10)
    driver.close()