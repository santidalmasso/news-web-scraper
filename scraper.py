import logging
import re
from news_page import HomePage, ArticlePage
from common import config
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

logging.basicConfig(level=logging.INFO)

class Scraper:

  _is_well_formed_link = re.compile(r'^https?://.+/.+$')
  _is_root_path = re.compile(r'^/.+$')

  def __init__(self, site_uid):
    self.site_uid = site_uid
    self.host = config()['news_sites'][site_uid]['url']

    logging.info('Beginning scraper for {}'.format(self.host))
    self.home_page = HomePage(site_uid, self.host)
    self.articles = []

  def execute(self):
    for link in self.home_page.article_links:
      article = self._fetch_article(link)
      if article:
        logging.info('Article fetched!')
        self.articles.append(article)
          

  def _fetch_article(self, link):
    logging.info('Start fetching article at {}'.format(link))

    article = None
    try:
      article = ArticlePage(self.site_uid, self._build_link(link))
    except (HTTPError, MaxRetryError) as e:
      logging.warning('Error while fetching the article', exc_info=False)
    
    if article and not article.body:
      logging.warning('Invalid article. There is no body')
      return None
    
    return article

  def _build_link(self, link):
    if self._is_well_formed_link.match(link):
      return link
    elif self._is_root_path.match(link):
      return '{}{}'.format(self.host, link)
    else:
      return '{host}/{uri}'.format(host=self.host, uri=link)

