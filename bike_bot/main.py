from os.path import dirname, abspath, join
import sys

CURRENT_DIR = dirname(__file__)
SCRAPER_DIR = abspath(join(CURRENT_DIR, '..' , "Kijiji-Scraper"))
sys.path.append(SCRAPER_DIR)

import re

from kijiji_scraper.kijiji_scraper import KijijiScraper


url = '''https://www.kijiji.ca/b-markham-york-region/bikes/k0l1700274?ll=43.879401%2C-79.414110&address=23+Farmstead+Rd%2C+Richmond+Hill%2C+ON+L4S+1V8%2C+Canada&radius=50.0&dc=true'''

if __name__ == "__main__":
    keywords = ["giant", "norco", "jamis", "trek", "\bgt\b", "specialized", "liv", "cannondale", "marin"]
    # Compile regex expressions for speed
    compiled = keywords.map(re.compile)
        
    scraper = KijijiScraper()
    ads, email_title = scraper.scrape_kijiji_for_ads(url)
    key_ads = {}


    for ad in ads:
        if 
    '''
    ads is a dictionary type
    Keys are ad ID's
    Values are INFO dictionaries

    info = {
        Title:
        Image:
        Url:
        Details:
        Description:
        Date:
        Location:
        Price:
        DataSource:
    }
    '''
    scraper.save_ads()

