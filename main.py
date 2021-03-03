import argparse
from common import config
from news_page import HomePage
from scraper import Scraper

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  news_sites_choises = list(config()['news_sites'].keys())
  
  parser.add_argument('news_site',
                      help='The news site that you want to scrape',
                      type=str,
                      choices=news_sites_choises)
  args = parser.parse_args()
  scraper = Scraper(args.news_site)
  scraper.execute()