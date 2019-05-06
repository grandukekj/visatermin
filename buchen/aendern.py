from selenium import webdriver
from userInfo import *
from emailAlert import *
import time

userinfos = load_userinfo()

# personal infos
GebJahr = userinfos.gebDatum[:4]
GebMon = userinfos.gebDatum[5:7]
GebTag = userinfos.gebDatum[8:]

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
# chrome_driver = os.getcwd() +"\\chromedriver.exe"

driver = webdriver.Chrome()
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get(
    "https://formular.berlin.de/xima-forms-29/get/14963116144270000?mandantid=/OTVBerlin_LABO_XIMA/000-01"
    "/instantiationTasks.properties")

try:
    # click on 'appointment change'
    driver.find_element_by_xpath('//*[@id="btnTerminAendern"]').click()
    # first name
    driver.find_element_by_xpath('//*[@id="tfFirstName"]').send_keys(userinfos.vorname)
    # last name
    driver.find_element_by_xpath('//*[@id="tfLastName"]').send_keys(userinfos.nachname)
    # birthdate: day
    driver.find_element_by_xpath('//select[@id="cobGebDatumTag"]/option[text() = %s]' % GebTag).click()
    # birthdate: month
    driver.find_element_by_xpath('//select[@id="cobGebDatumMonat"]/option[text() = %s]' % GebMon).click()
    # birthdate: year
    driver.find_element_by_xpath('//*[@id="tfGebDatumJahr"]').send_keys(GebJahr)
    # Vorgangsnummer
    driver.find_element_by_xpath('//*[@id="tfVorgangsnummer"]').send_keys(userinfos.vorgangsnummer)
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

except:
    time.sleep(10)
    driver.close()