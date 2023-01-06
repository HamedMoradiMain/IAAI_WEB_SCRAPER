try:
    import os # os module 
    import sys # sys module
    from selenium import webdriver # webdriver
    from selenium.webdriver import Chrome # chrome 
    from selenium.webdriver.common.keys import Keys # keys
    from selenium.webdriver.common.by import By # by
    from selenium.webdriver.support.ui import WebDriverWait # webdriverwait
    from selenium.webdriver.support import expected_conditions # expected conditions
    from selenium.common.exceptions import TimeoutException # time out exception
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC # options
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    import time # time module 
    import re
    import json
    import random
    import requests # request img from web
    import shutil # save img locally
    import requests 
    from bs4 import BeautifulSoup
    import re
except ModuleNotFoundError as e:
    print(e)
class Scraper:
    links = []
    def main(self):
        headers = {
            'authority': 'l.clarity.ms',
            'accept': 'application/x-clarity-gzip',
            'accept-language': 'en,fa;q=0.9,en-US;q=0.8,tr;q=0.7',
            # 'cookie': 'MUID=247B53299399642D0D2C41A7921265A8',
            'dnt': '1',
            'origin': 'https://www.iaai.com',
            'referer': 'https://www.iaai.com/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            }
        res = requests.get("https://www.iaai.com/Search?url=awszrp3nqcGcUzqHq8lDtF5TKWcKWo6PHrCPlnY6O1Y%3d",headers=headers)
        if res.status_code == 200:
            bs_obj = BeautifulSoup(res.content,features="html.parser")
            links = bs_obj.find_all("a",{"class":re.compile("link link-no-style")})
            for link in links:
                if link['href'] not in self.links:
                    self.links.append(link['href'])
                    print(link['href'])
    def desc_scraper(self,link):
        
    def run(self):
        '''self.main()
        with open("links.txt","w",encoding="utf-8") as f:
            for item in self.links:
                f.write(item)
                f.write("\n")
            f.close()'''
        self.desc_scraper("https://www.iaai.com/VehicleDetail/35975514~US")
if __name__ == "__main__":
    bot = Scraper()
    bot.run()