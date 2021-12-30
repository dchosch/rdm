# My wife regularly sells and purchases stuff on thi online platform. Of course
# she uses the free service, which means that if you want to appear somewhere
# at the top of the search results, you need to take down and put up your ad on
# a weekly basis. We have a guest bed we've been trying to get rid off for a
# while now and she has been doing this mennial task for some weeks now. So I
# decided to write a bot for her to automate the task. I don't think a bot is an
# issue in this particular example as it's used to upload single ads at a time.
# We are not overloading anyone's server.
#
# A word on the package used here. I had a quick look into Selenium and used it
# to build the bot quickly. Nothing fancy really but maybe it inspires you!
#
# I created a short cockpit area for my wife to type in the needed details for
# the program to run without her having to bother with the code. One issue I
# encountered is interacting with the 'upload files' hurdle on this parcitular
# site. In this iteration I didn't find a quick way to automate this step. This
# seems to be a common theme out there. I'm sure I'll circle back to it in some
# time an try to get that splinter out my brain. :)
#
# One last thing, I affectionately named this program 'tuttibot' as the site my
# wife uses is called tutti. I thought it amusing (yes, I guess I a total geek).


###
# Cockpit
###

usrname = '*******@gmail.com'
pssword = '******'
title = 'Gästebett Doppelbett Herausziehbar Micasa superba Twin III'
price = '400'
description = 'Gästebett von Micasa (mydream by superba TWIN III)\n\nZwei Einzelbetten, das untere kann herausgezogen (hat Rollen) und aufgeklappt werden. Ist leicht aufzustellen und wieder wegzuräumen, beide Betten gleich hoch, inklusive Lattenrost (bei oberem Bett kann Kopfteil verstellt werden), sehr stabil, sehr gute Qualität\n\nNeupreis: 850.-\n\nHat Gebrauchsspuren (siehe Fotos: zwei Plastikteile mussten wir kleben und eine Latte), aber funktioniert einwandfrei. Wir verkaufen es nur, weil wir keinen Platz mehr dafür haben. Ohne Matratzen.\n\nTierfreier, Nichtraucher Haushalt.'
t = 25

### Code below ###

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

PATH = '/Applications/chromedriver'
drv = webdriver.Chrome(PATH)

# Open site
drv.get('https://www.tutti.ch/de/start/login')
time.sleep(2)

# Get rid of cookie prompt
drv.find_element_by_id('onetrust-accept-btn-handler').click()

# Log in
drv.find_element_by_name('email').send_keys('usrname')
psswd = drv.find_element_by_name('password')
psswd.send_keys('pssword')
psswd.send_keys(Keys.RETURN)
time.sleep(2)

###
# Inserat runternehmen
###
drv.find_elements_by_class_name('_1D7pc')[2].click()
drv.find_elements_by_class_name('_3h3iN')[2].click()
drv.find_element_by_class_name('uisSB').click()
time.sleep(2)

###
# Inserat aufgeben
###
drv.find_element_by_id('insertAdId').click()
time.sleep(2)

# 1/5
# Kategorie: Haushalt
drv.find_elements_by_class_name('_29uuI')[0].click()
drv.find_elements_by_class_name('_3qfbp')[10].click()
# Unterkategorie: Möbel
drv.find_elements_by_class_name('_29uuI')[1].click()
drv.find_elements_by_class_name('_3qfbp')[28].click()
# Typ: Angebot
drv.find_elements_by_class_name('_29uuI')[2].click()
drv.find_elements_by_class_name('_3qfbp')[30].click()
# Fotos auswählen
btn = drv.find_element_by_class_name('_7KflF')
btn.click()
time.sleep(t)
#btn.send_keys('/Users/dnl/Desktop/pic1.jpeg') # auto-upload failed!
# Nächste Seite
drv.find_element_by_class_name('_1jvck').click()
time.sleep(2)

# 2/5
# Preis
drv.find_element_by_id('3-1-2-val-text-input').send_keys(price)
# Titel
drv.find_element_by_id('3-1-3-val-text-input').send_keys(title)
# Beschreibung
drv.find_element_by_id('textarea_body').send_keys(description)
# Nächste Seite
time.sleep(2)
drv.find_element_by_class_name('_1jvck').click()
time.sleep(2)

# 3/5
# Nächste Seite
time.sleep(1)
drv.find_element_by_class_name('_1jvck').click()
time.sleep(2)

# 4/5
# Nächste Seite
drv.find_element_by_class_name('_1jvck').click()
time.sleep(2)

# 5/5
drv.find_element_by_id('aiSubmitFree').click()
time.sleep(5)

# Log out
drv.find_element_by_class_name('sc-uu0ihi-2').click()
drv.find_element_by_class_name('sc-15roptm-9').click()
time.sleep(2)

# Close site
drv.quit()
