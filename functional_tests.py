# -*- coding=utf-8 -*-
"""functional testing for bioweb application"""

import sys
import os
import time
import unittest
import re
import subprocess
from splinter import Browser
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

##find_by_type
def findByType(browser, ident, type):
    if type != 'css' and type != 'xpath' and type != 'tag' and type != 'id' and type != 'text' and type != 'name' and type != 'href':
        error = "Improper search method " + str(type)
        self.assertTrue(False, error)
    if(type == 'css'):
        return browser.find_by_css(ident)
    elif(type == 'xpath'):
        return browser.find_by_xpath(ident)
    elif(type == 'tag'):
        return browser.find_by_tag(ident)
    elif(type == 'text'):
        return browser.find_by_text(ident)
    elif(type == 'id'):
        return browser.find_by_id(ident)
    elif(type == 'name'):
        return browser.find_by_name(ident)
    elif(type == 'href'):
        return browser.find_link_by_href(ident)
    return

## @brief test-cases

class TestFunctionalBioweb(unittest.TestCase):

    ## Browser used for testing - default Google Chrome
    browser = ''

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def clickMenuLink(self, ident, interval=0.1, maxTime=1.0, type='css'):
        """Searches for an identifier and clicks it. Search method is provided by 'type' argument
          - either css, xpath, tag, text, id, href or name."""
        counter = 0.0
        link = None
        while counter < maxTime and link is None:
            try:
                link = findByType(self.browser, ident, type)
            except:
                time.sleep(interval)
                counter += interval
        self.assertIsNotNone(link, "Cannot find link with ident='{css}' in {brow}".format(css=ident, brow='self.browser'))
        link.first.click()

    def findElement(self, ident, interval=0.1, maxTime=1, type='css'):
        """Searches for an identifier and returns it. Search method is provided by 'type' argument
          - either css, xpath, tag, text, id, href or name."""
        counter = 0.0
        link = None
        while counter < maxTime and link is None:
            try:
                link = findByType(self.browser, ident, type)
            except:
                time.sleep(interval)
                counter += interval
        self.assertIsNotNone(link, "Cannot find link with ident='{css}' in {brow}".format(css=ident, brow='self.browser'))
        return link.first

    def test01AnyAnswer(self):
        """tests if the application is loaded"""
        self.assertTrue(len(self.browser.html) > 0)

    def test02ProperTitleAndLogo(self):
        """tests if the web page title and logo is correct"""
        title = self.browser.title
        if not isinstance(title, str):
            title = title.decode()
        self.assertEqual(title, u'Conway\'s Game of Life')

    def test03TabTranslations(self):
        """test if translations works"""
        self.clickMenuLink('#a_lang_en')
        self.assertEqual(self.findElement('gameLabel', type='id').text[:len('Conway\'s Game of Life')], u'Conway\'s Game of Life')
        self.assertEqual(self.findElement('evolveBtn', type='id').text[:len('Evolve')], u'Evolve')
        self.assertEqual(self.findElement('startBtn', type='id').text[:len('Start simulation')], u'Start simulation')
        self.assertEqual(self.findElement('stopBtn', type='id').text[:len('Stop simulation')], u'Stop simulation')

        self.clickMenuLink('#a_lang_pl')
        self.assertEqual(self.findElement('gameLabel', type='id').text[:len('Gra w życie')], u'Gra w życie')
        self.assertEqual(self.findElement('evolveBtn', type='id').text[:len('Ewoluuj')], u'Ewoluuj')
        self.assertEqual(self.findElement('evolveBtn', type='id').text[:len('Rozpocznij symulację')], u'Rozpocznij symulację')
        self.assertEqual(self.findElement('evolveBtn', type='id').text[:len('Zatrzymaj symulację')], u'Zatrzymaj symulację')

    def test05CppEvolve(self):
        """test new command creation"""
        self.assertTrue(self.findElement('generationCountParagraph', type='id').text[-1], "0");
        self.clickMenuLink('evolveBtn', type='id');
        time.sleep(1)
        self.assertTrue(self.findElement('generationCountParagraph', type='id').text[-1], "1");
        self.clickMenuLink('evolveBtn', type='id');
        time.sleep(1)
        self.assertTrue(self.findElement('generationCountParagraph', type='id').text[-1], "2");

if __name__ == "__main__":
    ## Browser used in the tests
    www_browser = 'chrome'
    ## Webpage address
    www_addr = '127.0.0.1'
    ## Port used
    www_port = '9000'
    ## Test mode - f for localhost, g for demo server
    mode = ''
    if len(sys.argv) == 4:
        www_browser = sys.argv[1]
        www_addr = sys.argv[2]
        www_port = sys.argv[3]
    if www_browser == 'google-chrome' or www_browser == 'google-chrome-stable':
        www_browser = 'chrome' #  Drivers only recognize 'chrome' as a name

    browser = Browser(www_browser)
    browser.driver.maximize_window()
    address = 'http://' + www_addr + ':' + www_port
    browser.visit(address)

    # setting up the class
    TestFunctionalBioweb.browser = browser

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFunctionalBioweb))

    try:
        unittest.TextTestRunner(verbosity=3).run(suite)
    finally:
        pass

    browser.quit()
