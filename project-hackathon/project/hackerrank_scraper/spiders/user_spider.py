import scrapy
import json
from ..items import HackerRankUserItem
from datetime import datetime
from dateutil import parser

class UserSpider(scrapy.Spider):
    name = 'hackerrank_user'
    
    def __init__(self, username=None, *args, **kwargs):
        super(UserSpider, self).__init__(*args, **kwargs)
        if not username:
            raise ValueError("Username is required")
        self.username = username
        self.start_urls = [f'https://www.hackerrank.com/{username}']
    
    def parse(self, response):
        # Extract the script containing user data
        script_content = response.xpath('//script[contains(text(), "userData")]/text()').get()
        if not script_content:
            self.logger.error(f"No data found for user: {self.username}")
            return
        
        # Extract JSON data from script
        try:
            json_str = script_content.split('userData = ')[1].split(';\n')[0]
            user_data = json.loads(json_str)
            
            item = HackerRankUserItem()
            item['username'] = user_data.get('name', self.username)
            item['overall_rank'] = user_data.get('overall_rank', 'N/A')
            item['badges'] = len(user_data.get('badges', []))
            item['leaderboard_rank'] = user_data.get('leaderboard_rank', 'N/A')
            
            # Parse last submission date
            last_submission = user_data.get('last_submission_at')
            if last_submission:
                item['last_submission'] = parser.parse(last_submission).strftime('%Y-%m-%d')
            else:
                item['last_submission'] = 'N/A'
                
            yield item
            
        except (json.JSONDecodeError, IndexError) as e:
            self.logger.error(f"Error parsing data: {str(e)}")