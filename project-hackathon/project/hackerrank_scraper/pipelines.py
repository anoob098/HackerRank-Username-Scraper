from tabulate import tabulate

class HackerRankPipeline:
    def process_item(self, item, spider):
        # Convert item to table format
        headers = ['Username', 'Overall Rank', 'Badges', 'Leaderboard Rank', 'Last Submission']
        data = [[
            item['username'],
            item['overall_rank'],
            item['badges'],
            item['leaderboard_rank'],
            item['last_submission']
        ]]
        
        # Print table
        print("\nHackerRank User Profile")
        print(tabulate(data, headers=headers, tablefmt='grid'))
        return item