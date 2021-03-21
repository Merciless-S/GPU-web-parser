import requests
from bs4 import BeautifulSoup
import webbrowser
import _thread
from time import sleep
import random
import os
from datetime import datetime


class Parser:
    def get_page_html(self, url):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        try:
            page = requests.get(url, headers = headers)
        except:
            print("error fetching url", url)
            return None
        return page.content
    
    def check_item_in_stock(self, page_html, isAMD):
        soup = BeautifulSoup(page_html, 'html.parser')
        if isAMD:
            out_of_stock_divs = soup.findAll("p", {"class": "product-out-of-stock"})
        else:
            out_of_stock_divs = soup.findAll("button", {"class": "btn btn-disabled btn-lg btn-block add-to-cart-button"})  
        #print(out_of_stock_divs)
        return len(out_of_stock_divs) == 0
    
    def check_inventory(self, url, isAMD):
        page_html = self.get_page_html(url)
        if page_html == None:
            return False
        return self.check_item_in_stock(page_html, isAMD)
    
    
    def check(self, url, isAMD = False):
        while not self.check_inventory(url, isAMD):
            if isAMD:
                self.amd_count += 1
            else:
                self.bestbuy_count += 1
            sleep(1 + random.random())
            #print("checking ", url)
        _thread.start_new_thread(self.write, (url,) )
        webbrowser.open_new(url)
    
    def write(self, url):
        file = open("found.txt", "a+")
        file.write(url + "\n")
        file.write(datetime.now().strftime("%H:%M:%S") + "\n")
        file.close()
        
    def clear(self):
        while 1:
            sleep(20)
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def display(self):
        _thread.start_new_thread(self.display1(), () )
        
    def display1(self):
        while 1:
            print("Best buy has been checked", self.bestbuy_count, "times")
            print("AMD has been checked", self.amd_count, "times")
            sleep(10)
        
    def __init__(self):
        self.amd_count = 0
        self.bestbuy_count = 0
        self.bestbuy = ["https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402",
                "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440",
                "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-xc-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444445.p?skuId=6444445",
                "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
                "https://www.bestbuy.com/site/evga-geforce-rtx-3070-ftw3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439301.p?skuId=6439301",
                "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439300.p?skuId=6439300",
                "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436196.p?skuId=6436196",
                "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400",
                "https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432658.p?skuId=6432658",
                "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6800xt-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6441226.p?skuId=6441226",
                "https://www.bestbuy.com/site/msi-amd-radeon-rx-6800-xt-16g-16gb-gddr6-pci-express-4-0-graphics-card-black/6440913.p?skuId=6440913",
                "https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6800-gaming-oc-16gb-gddr6-pci-express-4-0-graphics-card/6453897.p?skuId=6453897",
                "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-ftw3-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444444.p?skuId=6444444",
                "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434"
                ]
        self.AMD = [
               "https://www.amd.com/en/direct-buy/5458373400/us",
               "https://www.amd.com/en/direct-buy/5458372800/us",
               "https://www.amd.com/en/direct-buy/5496921400/us",
               ]
        '''
        try:
            for url in self.bestbuy:
                _thread.start_new_thread(self.check, (url,) )
            for url in self.AMD:
                _thread.start_new_thread(self.check, (url, True) )
        except:
            print("Error: unable to start thread")
        '''
        
    def checkBestBuy(self):
        try:
            for url in self.bestbuy:
                _thread.start_new_thread(self.check, (url,) )
                _thread.start_new_thread(self.check, (url,) )
        except:
            print("Error: unable to start thread for Best Buy")
            
    def checkAMD(self):
        try:
            for url in self.AMD:
                _thread.start_new_thread(self.check, (url, True) )
                _thread.start_new_thread(self.check, (url, True) )
        except:
            print("Error: unable to start thread for AMD")
            
            
def __main__():
    parser = Parser()
    parser.checkBestBuy()
    parser.checkAMD()
    parser.display()
    
if __name__ == "__main__":
    __main__()