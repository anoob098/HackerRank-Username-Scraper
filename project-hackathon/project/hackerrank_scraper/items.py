from scrapy import Item, Field

class HackerRankUserItem(Item):
    username = Field()
    overall_rank = Field()
    badges = Field()
    leaderboard_rank = Field()
    last_submission = Field()