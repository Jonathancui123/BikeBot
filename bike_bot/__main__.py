from os.path import dirname, abspath, join
import sys
import re
from bike_bot.services.read_write_files import loadSavedAds, output_json, load_json
from bike_bot import constants

def checkAdInfoKeywords(keywords: list, adInfo: dict) -> bool:
    ''' Checks the title, details, and description of the adInfo for patterns '''
    components = [adInfo['Title'], adInfo['Details'], adInfo['Description']]

    for component in components:
        for keyword in keywords:
            if re.search(keyword, component):
                return True
    
    return False

def outputKeywordAds():
    ''' Loads ads and outputs a file with only ads that contain keywords'''
    ads = loadSavedAds()
    key_ads = {}

    print("Matching keywords...")
    for adId, adInfo in ads.items():
        if checkAdInfoKeywords(constants.keywords, adInfo):
            key_ads[adId] = adInfo
    print(f"Found {len(key_ads)} ads out of {len(ads)} that matched keywords")
    output_json(key_ads)

def scrapeAllAds():
    '''Update ads.json with all the newest ads from the given URL'''

    CURRENT_DIR = dirname(__file__)
    SCRAPER_DIR = abspath(join(CURRENT_DIR, '..' , "Kijiji-Scraper"))
    sys.path.append(SCRAPER_DIR)

    from kijiji_scraper.kijiji_scraper import KijijiScraper

    scraper = KijijiScraper()
    ads, email_title = scraper.scrape_kijiji_for_ads(constants.url)
    scraper.save_ads()
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

if __name__ == "__main__":
    outputKeywordAds()
    

