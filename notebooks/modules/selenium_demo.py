import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://www.dr.dk/'


def firefox_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir', os.getcwd())
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

    logging.info('Prepared firefox profile..')

    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    logging.info('Initialized firefox browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()

if __name__ == '__main__':
    firefox_example()