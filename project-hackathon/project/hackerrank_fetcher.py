import json
import sys
import urllib.request
import urllib.error
from datetime import datetime

def create_table(headers, data):
    """Create a simple ASCII table"""
    # Calculate column widths
    widths = [len(header) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    
    # Create separator line
    separator = '+' + '+'.join('-' * (w + 2) for w in widths) + '+'
    
    # Create header
    result = [separator]
    header_row = '|' + '|'.join(f' {h:<{w}} ' for h, w in zip(headers, widths)) + '|'
    result.append(header_row)
    result.append(separator)
    
    # Create data rows
    for row in data:
        data_row = '|' + '|'.join(f' {str(c):<{w}} ' for c, w in zip(row, widths)) + '|'
        result.append(data_row)
    
    result.append(separator)
    return '\n'.join(result)

def fetch_user_data(username):
    """Fetch user data from HackerRank API"""
    url = f'https://www.hackerrank.com/rest/contests/master/hackers/{username}/profile'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())
            return data['model']
    except urllib.error.URLError as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing response: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: User data not found")
        sys.exit(1)

def format_date(date_str):
    """Format date string to YYYY-MM-DD"""
    if not date_str:
        return 'N/A'
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        return dt.strftime('%Y-%m-%d')
    except ValueError:
        return 'N/A'

def main():
    if len(sys.argv) != 2:
        print("Usage: python hackerrank_fetcher.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"\nFetching data for user: {username}")
    
    try:
        user_data = fetch_user_data(username)
        
        # Prepare data for table
        headers = ['Username', 'Overall Rank', 'Badges', 'Leaderboard Rank', 'Last Submission']
        data = [[
            user_data.get('username', username),
            user_data.get('overall_rank', 'N/A'),
            len(user_data.get('badges', [])),
            user_data.get('leaderboard_rank', 'N/A'),
            format_date(user_data.get('last_submission_at'))
        ]]
        
        # Display table
        print("\nHackerRank User Profile")
        print(create_table(headers, data))
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()