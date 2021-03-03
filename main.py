import argparse
from common import config

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  news_sites_choises = list(config()['news_sites'].keys())
  
  parser.add_argument('news_site',
                      help='The news site that you want to scrape',
                      type=str,
                      choices=news_sites_choises)
  args = parser.parse_args()
  print(config()['news_sites'][args.news_site]['url'])