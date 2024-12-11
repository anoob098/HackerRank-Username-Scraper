"""API client for fetching HackerRank user data."""

import http.client
import json
from . import config

class HackerRankAPIClient:
    @staticmethod
    def fetch_user_data(username):
        """Fetch user data from HackerRank API."""
        conn = http.client.HTTPSConnection(config.API_BASE_URL)
        headers = {"User-Agent": config.USER_AGENT}
        
        try:
            path = config.API_PATH.format(username=username)
            conn.request("GET", path, headers=headers)
            response = conn.getresponse()
            
            if response.status != 200:
                raise Exception(f"API request failed with status {response.status}")
            
            data = json.loads(response.read().decode())
            return data.get('model', {})
            
        except Exception as e:
            raise Exception(f"Failed to fetch user data: {str(e)}")
        finally:
            conn.close()