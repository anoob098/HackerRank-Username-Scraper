"""Process and format HackerRank user data."""

from datetime import datetime

class DataProcessor:
    @staticmethod
    def format_date(date_str):
        """Format date string to YYYY-MM-DD."""
        if not date_str:
            return 'N/A'
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            return dt.strftime('%Y-%m-%d')
        except ValueError:
            return 'N/A'
    
    @staticmethod
    def process_user_data(user_data, username):
        """Process raw user data into display format."""
        return {
            'username': user_data.get('username', username),
            'overall_rank': user_data.get('overall_rank', 'N/A'),
            'badges': len(user_data.get('badges', [])),
            'leaderboard_rank': user_data.get('leaderboard_rank', 'N/A'),
            'last_submission': DataProcessor.format_date(user_data.get('last_submission_at'))
        }