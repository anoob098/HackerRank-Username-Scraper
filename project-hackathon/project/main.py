"""Main entry point for the HackerRank user data fetcher."""

import sys
from src.api_client import HackerRankAPIClient
from src.data_processor import DataProcessor
from src.table_formatter import TableFormatter

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"\nFetching data for user: {username}")
    
    try:
        # Fetch data
        user_data = HackerRankAPIClient.fetch_user_data(username)
        
        # Process data
        processed_data = DataProcessor.process_user_data(user_data, username)
        
        # Prepare table data
        headers = ['Username', 'Overall Rank', 'Badges', 'Leaderboard Rank', 'Last Submission']
        data = [[
            processed_data['username'],
            processed_data['overall_rank'],
            processed_data['badges'],
            processed_data['leaderboard_rank'],
            processed_data['last_submission']
        ]]
        
        # Display table
        print("\nHackerRank User Profile")
        print(TableFormatter.create_table(headers, data))
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()