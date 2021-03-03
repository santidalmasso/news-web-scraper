import bs4
import requests

from common import config

class NewsPage:

  def __init__(self, news_site_uid, url):
    self._config = config()['news_sites'][news_site_uid]
    self._queries = self._config['queries']
    self._html = None

    self._visit(url)
  
  def _select(self, query_string):
    return self._html.select(query_string)
  
  def _visit(self, url):
    r = requests.get(url)

    r.raise_for_status()

    self._html = bs4.BeautifulSoup(r.text, 'html.parser')


class HomePage(NewsPage):

  def __init__(self, news_site_uid, url):
    super().__init__(news_site_uid, url)

  @property
  def article_links(self):
    link_list = []
    article_links_elements = self._select(self._queries['homepage_article_links'])

    for link in article_links_elements:
      if link and link.has_attr('href'):
        link_list.append(link)
    
    return set(link['href'] for link in link_list)
