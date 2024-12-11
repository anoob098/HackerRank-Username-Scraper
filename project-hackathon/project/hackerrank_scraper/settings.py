BOT_NAME = 'hackerrank_scraper'

SPIDER_MODULES = ['hackerrank_scraper.spiders']
NEWSPIDER_MODULE = 'hackerrank_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'hackerrank_scraper.pipelines.HackerRankPipeline': 300,
}

# Set default headers
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}