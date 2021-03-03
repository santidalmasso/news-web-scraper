import argparse
from common import config
from news_page import HomePage

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  news_sites_choises = list(config()['news_sites'].keys())
  
  parser.add_argument('news_site',
                      help='The news site that you want to scrape',
                      type=str,
                      choices=news_sites_choises)
  args = parser.parse_args()
  for title in HomePage(args.news_site ,config()['news_sites'][args.news_site]['url']).article_links:
    print(title)