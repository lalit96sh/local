"""
Basic High Level implementation for Web Crawler
"""

# some helper functions


class Helper:
    
    @classmethod
    def get_contents_of_url(url):
        """extracts contents of url
        """
    @classmethod
    def get_signature_of_url(url):
        """extracts contents of url
        """
    
    @classmethod
    def extract_urls_in_page_with_url(url):
        """extracts contents of url
        """

class Page:
    def __init__(self, url):
        """basic url components
        """
        self.url = url
        self.set_page()
    
    def set_page(self):
        self.contents = Helper.get_contents_of_url(self.url)
        self.signature = Helper.get_signature_of_url(self.url)
        self.child_urls = Helper.extract_urls_in_page_with_url(self.url)

# class DocStore:
#     def __init__(self):
#         """setup basic page details to be fetched later, when user searches
#         """
        

class DataStore:
    
    def __init__(self,db):
        self.db = db
        """
        Define basic components for Page data store
        """
    
    def pop_max_priority_url(self):
        """Returns Max priority Page from database
        """
        
    def insert_into_crawled_url(self, url, signature):
        """Insert the url into crawled links
        """
        
    def insert_into_urls_to_crawl(self, url):
        """insert url into urls which needs to crawl

        """
        
    def is_crwaled_similar(self,signature):
        """check if we have crawled the page with similar signature
        """
    
    def decrease_priority_urls_to_crawl(self,url):
        """decrease priority and append into queue again
        """

class ReverseIndexeQueue:
    def __init__(self):
        """
        Set a queue, It will be used by Service to get and create snippets with respect to words in contents
        """
        import collections
        self.queue = collections.deque()
    
    def get_first(self):
        self.queue.popleft()
    def append(self,page):
        self.queue.append(page)
        
class Crawler:
    def __init__(self,data_store,reverse_index_queue, doc_index_queue):
        self.data_store = data_store
        self.reverse_index_queue = reverse_index_queue
        self.doc_index_queue = doc_index_queue
    
    def crawl_page(self, page):
        
        for url in page.child_urls:
            self.data_store.insert_into_urls_to_crawl(url)
        
    
    def crawl(self):
        while True:
            url = self.data_store.pop_max_priority_url()
            if url is None:
                break
            page = Page(url)
            
            if self.data_store.is_crwaled_similar(page.signature):
                self.data_store.decrease_priority_urls_to_crawl(url)
            else:
                self.crawl_page(page=page)
                self.insert_into_crawled_url(url)
                self.reverse_index_queue.append(page)

class CrawlerOperationService:
    def __init__(self, crawler, words_db):
        self.crawler = crawler
        self.words_db = words_db
    def extract_words_and_snippet_from_page(self, page):
        """create words from page contents and put them into db
        """
    
    
    
    