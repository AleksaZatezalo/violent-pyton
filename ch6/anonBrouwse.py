"""
Description: A python script to tunnel browser traffic trhough a vpn.
Author: Aleksa Zatezalo
Date: June 29th, 2023
"""

import mechanize
from mechanize._html import Factory
import cookielib
import random
import time

class anonBrowser(mechanize.Browser):
    def __init__(self, proxies = [], user_agents = []):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(self)
        self.proxies = proxies
        self.user_agents = user_agents + ['Mozilla/4.0', 'FireFox/6.01', 'ExactSearch', 'Nokia7110/1.0']
        self.cookiejar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookiejar)
        self.anonymize()

    def clear_cookies(self):
        self.cookiejar = cookielib.LWPCookieJaR()
        self.set_cookiejar(self.cookiejar)
    
    def change_user_agents(self):
        index = random.randrange(0, len(self.proxies))
        self.addheaders = [('User-agent', self.user_agents(index))]

    def change_proxies(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies({'http': self.proxies[index]})

    def anonymize(self, sleep=False):
        self.clear_cookies()
        self.change_user_agents()
        self.change_proxies()
        if sleep:
            time.sleep(60)